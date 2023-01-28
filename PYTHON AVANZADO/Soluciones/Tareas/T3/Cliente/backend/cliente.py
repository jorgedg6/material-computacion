"""
Modulo contiene implementación principal del cliente
"""
import socket
from sys import byteorder
from threading import Thread
from backend.logica import Logica
from PyQt5.QtCore import pyqtSignal
import json
from PyQt5.QtCore import QObject

class Cliente(QObject):

    senal_confirmacion_login = pyqtSignal()
    senal_denegacion_login = pyqtSignal()
    senal_actualizar_usuarios = pyqtSignal(tuple)

    def __init__(self, host, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Logica(self)
        self.nombre = None
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
        except ConnectionError as error:
            print(f"Error: {error}")
        except ConnectionRefusedError as error2:
            print(f"Error: {error2}")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()
        print("Empezando a escuchar al servidor...")

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    print(mensaje)
                    self.manejar_mensaje(mensaje)
        except ConnectionError as e:
            print(f"Error: {e}")

    def manejar_mensaje(self, mensaje):
        comando = mensaje['comando']
        if comando == 'usuario_valido':
            self.senal_confirmacion_login.emit()
            self.senal_actualizar_usuarios.emit((mensaje['usuarios'], mensaje['administrador']))
            pass
        elif comando == 'usuario_invalido':
            self.senal_denegacion_login.emit()
            self.usuario = None
            pass

    def recibir(self):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder="little")
        for _ in range(largo_mensaje):
            self.socket_cliente.recv(4)
            full, length = self.socket_cliente.recv(2)
            if full == 1:
                bytes_mensaje += self.socket_cliente.recv(20)
            else:
                bytes_mensaje += self.socket_cliente.recv(length)
        #final = self.desencriptar_mensaje(bytes_mensaje)
        if bytes_mensaje != b'':
            final = json.loads(bytes_mensaje)
            return final

    def enviar(self, diccionario):
        """
        Envía un mensaje a un cliente.
        """
        #bytes_mensaje = self.encriptar_mensaje(datos)
        #mensaje_codificado = self.codificar_mensaje(bytes_mensaje)
        mensaje_codificado = self.codificar_mensaje(diccionario)
        self.socket_cliente.sendall(mensaje_codificado)

    def encriptar_mensaje(self, mensaje):
        '''
        Encripta el mensaje a enviar
        '''
        #try:
        '''ENCRIPTACION AQUI'''
        #####
        mensaje = json.dumps(mensaje)
        #####
        b_array = bytearray(mensaje.encode('utf-8'))
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
        #except:
        print("ERROR: No se pudo encriptar el mensaje")
        return b""

    def codificar_mensaje(self, msg_bytes):
        '''
        Codifica el mensaje a enviar
        '''
        #try:
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
        #except:
        print("ERROR: No se pudo codificar el mensaje")
        return b""

    def desencriptar_mensaje(self, mensaje_bytes):
        '''
        Desencripta el mensaje a enviar
        '''
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
            #print("ERROR: No se pudo desencriptar el mensaje")
            return {}