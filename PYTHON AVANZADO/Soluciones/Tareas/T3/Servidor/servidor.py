"""
Modulo contiene la implementación principal del servidor
"""
import socket
import threading
from Cliente.utils import data_json
from logica import Logica
import json
from random import choice

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.id_cliente = 0
        self.clientes_conectados = {}
        self.clientes_nombres = []
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.colores = [['R', True], ['G', True], ['B', True], ['Y', True]]
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True  # cambiar estado del servidor a conectado

        self.log(
            f"Servidor escuchando en puerto {self.port} y host {self.host}")
        self.comenzar_a_aceptar()

    def comenzar_a_aceptar(self):
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        while self.conectado and self.id_cliente <= data_json('MAXIMO_JUGADORES') - 1:
            try:
                socket_cliente, direccion = self.socket_servidor.accept()
                self.log(f"Direccion cliente {direccion}")
                thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(
                    self.id_cliente, socket_cliente), daemon=True)
                thread_cliente.start()
                self.clientes_conectados[self.id_cliente] = socket_cliente
                self.id_cliente += 1
            except ConnectionError:
                self.log("Error")

    def escuchar_cliente(self, id_cliente, socket_cliente):
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        try:
            while self.conectado and id_cliente <= 3:
                mensaje = self.recibir(socket_cliente)
                if not mensaje:
                    self.eliminar_cliente(id_cliente, socket_cliente)
                    raise ConnectionResetError
                respuesta = self.procesar_mensaje(
                    mensaje, socket_cliente)
                if respuesta:
                    self.enviar_mensaje(respuesta, socket_cliente)
        except (ConnectionResetError, ConnectionError) as error:
            self.log(f"Error: {error}")

    def enviar_todos(self, mensaje):
        for cliente in self.clientes_conectados:
            if self.clientes_conectados[cliente] != None:
                self.enviar_mensaje(mensaje, self.clientes_conectados[cliente])

    def procesar_mensaje(self, mensaje, socket_cliente):
        comando = mensaje['comando']
        if comando == 'chequeo_login':
            estado = self.chequear_login(mensaje)
            self.enviar_todos(estado)

    def chequear_login(self, mensaje):
        nombre = mensaje['nombre']
        pertenece = False
        for nombre_c in self.clientes_nombres:
            if nombre_c[0] == nombre:
                pertenece = True
        if nombre.isalnum() and 1 <= len(nombre) <= 10 and not pertenece:
            color_usuario = None
            while not color_usuario:
                color = choice(self.colores)
                if color[1]:
                    color[1] = False
                    color_usuario = color[0]
            if len(self.clientes_nombres) == 0:
                administrador = True
            else:
                administrador = False
            self.clientes_nombres.append([nombre, color_usuario])
            return {
                'usuarios': self.clientes_nombres,
                'administrador': administrador,
                'comando': 'usuario_valido'
            }
        else:
            return {'comando': 'usuario_invalido'}





    def recibir(self, socket_cliente):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder="little")
        for _ in range(largo_mensaje):
            socket_cliente.recv(4)
            full, length = socket_cliente.recv(2)
            if full == 1:
                bytes_mensaje += socket_cliente.recv(20)
            else:
                bytes_mensaje += socket_cliente.recv(length)
        #final = self.desencriptar_mensaje(bytes_mensaje)
        if bytes_mensaje != b'':
            final = json.loads(bytes_mensaje)
            return final

    def enviar_mensaje(self, diccionario, socket_cliente):
        #bytes_encriptados = self.encriptar_mensaje(mensaje)
        #bytes_mensaje = self.codificar_mensaje(bytes_encriptados)
        bytes_mensaje = self.codificar_mensaje(diccionario)
        socket_cliente.sendall(bytes_mensaje)

    def encriptar_mensaje(self, mensaje):
        try:
            '''ENCRIPTACION AQUI'''
            b_array = bytearray(mensaje, 'utf-8')
            a = b''
            b = b''
            i = 0
            orden = [0, 1, 0, 0, 1, 1]
            for byte in b_array:
                if orden[i] == 0:
                    a += byte.to_bytes(1, byteorder='big')
                elif orden[i] == 1:
                    b += byte.to_bytes(1, byteorder='big')
                #Rotación
                if i == 5:
                    i = 0
                else:
                    i += 1
            
            if len(a) % 2 == 0:
                n_a = a[len(a) // 2 - 1] + a[len(a) // 2]
            else:
                n_a = a[len(a) // 2] + (a[len(a) // 2 - 1] + a[len(a) // 2 + 1]) / 2
            
            if len(b) % 2 == 0:
                n_b = b[len(b) // 2 - 1] + b[len(b) // 2]
            else:
                n_b = b[len(b) // 2] + (b[len(b) // 2 - 1] + b[len(b) // 2 + 1]) / 2
            if n_a <= n_b:
                mensaje_bytes = (1).to_bytes(1, byteorder='big') + a + b
            elif n_a > n_b:
                mensaje_bytes = (0).to_bytes(1, byteorder='big') + b + a
            return mensaje_bytes
        except:
            print("ERROR: No se pudo encriptar el mensaje")
            return b""

    def desencriptar_mensaje(self, mensaje_bytes):
        try:
            '''DESENCRIPTACION AQUI'''
            modo = mensaje_bytes[0]
            mensaje_bytes = mensaje_bytes[1:]
            if modo == 1:
                a = 'hola'
                b = 'chao'
            elif modo == 2:
                b = 'hola'
                a = 'chao'
        except:
            print("ERROR: No se pudo desencriptar el mensaje")
            return {}

    def eliminar_cliente(self, id_cliente, socket_cliente):
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            # Desconectamos el usuario de la lista de jugadores
            self.clientes_conectados.pop(id_cliente, None)
            self.colores[id_cliente][1] = True
            self.clientes_nombres.pop(id_cliente)
            self.id_cliente -= 1
        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, msg_bytes):
        try:
            '''CODIFICACION AQUI'''
            mensaje = json.dumps(msg_bytes)
            msg_bytes = bytearray(mensaje.encode('UTF-8'))
            msg_final = bytearray()
            TAMANO_CHUNK = 20
            n_bloque = 0
            for i in range(0, len(msg_bytes), TAMANO_CHUNK):
                chunk = bytearray(msg_bytes[i:i+TAMANO_CHUNK])
                if len(chunk) < 20:
                    msg_final += (n_bloque).to_bytes(4, byteorder= "big") \
                                        + (0).to_bytes(1, byteorder= "big") \
                                            + (len(chunk)).to_bytes(1, byteorder= "big")
                elif len(chunk) == 20:
                    msg_final += (n_bloque).to_bytes(4, byteorder= "big") \
                                        + (1).to_bytes(1, byteorder= "big") \
                                            + (20).to_bytes(1, byteorder= "big")
                msg_final += chunk
                n_bloque += 1

            n_bloque_bytes = n_bloque.to_bytes(4, byteorder= "little")
            return n_bloque_bytes + msg_final
        except:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def log(self, mensaje: str):
        print("|" + mensaje.center(80, " ") + "|")
