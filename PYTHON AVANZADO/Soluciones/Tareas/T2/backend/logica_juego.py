#Imports PyQt
from PyQt5.QtWidgets import(
    QLabel
)
from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
    QTimer,
    QThread
    )
from PyQt5.QtGui import(
    QPixmap
)
from PyQt5.QtMultimedia import (
    QSound
)
#Imports Externos
from random import randint, choice
import sys
#Imports Locales
import parametros as p
from lectura import escribir
from backend.logica_mira import Mira
from backend.logica_alien import Alien

################## LOGICAJUEGO ##################

class LogicaJuego(QObject):

    senal_enviar_aliens = pyqtSignal(list)
    senal_enviar_mira = pyqtSignal(object)
    senal_cerrar_ventana = pyqtSignal(str)
    senal_post_juego = pyqtSignal(dict)
    senal_balas = pyqtSignal(str)
    senal_actualizar_tiempo = pyqtSignal(float)
    senal_label_termino = pyqtSignal(int)
    senal_pasar_nivel = pyqtSignal(int)
    senal_cambio_puntaje = pyqtSignal(int)
    senal_animacion_terminator_dog = pyqtSignal()
    senal_reset_sprite = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balas = 0
        self.crear_timers()
        self.puntaje = 0
        self.continua = False
        self.ponderador = 1
    
    def crear_aliens(self, tupla):
        '''
        Crea los aliens del nivel
        '''
        #Limpieza de lista de aliens
        self.aliens = []
        #Recepción del nivel actual
        self.usuario = tupla[0]
        self.nivel = tupla[1]
        self.balas = self.nivel * 4
        if self.nivel == 1:
            self.ponderador = p.PONDERADOR_TUTORIAL
        elif self.nivel == 2:
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO
        elif self.nivel == 3:
            self.ponderador = p.PONDERADOR_INVASION

        self.tiempo_restante = round((p.DURACION_NIVEL_INICIAL * self.ponderador) / 1000)
        #Instanciación de los aliens
        for _ in range(self.nivel):
            lista = []
            for _ in range(2):
                alien = Alien(self.nivel)
                lista.append(alien)
            self.aliens.append(lista)
        #Envío de señal a frontend
        self.senal_enviar_aliens.emit(self.aliens)
        self.aparecer_aliens()

    def cambiar_nivel(self, nivel):
        if nivel == 1:
            self.nivel = 2
            self.senal_cambio_puntaje.emit(self.puntaje)
            self.crear_aliens((self.usuario, self.nivel))
            self.continua = True
        elif nivel == 2:
            self.nivel = 3
            self.senal_cambio_puntaje.emit(self.puntaje)
            self.crear_aliens((self.usuario, self.nivel))
            self.continua = True

    def crear_timers(self):
        '''
        Crea los timers del juego
        '''
        #Timer termino juego
        self.timer_juego = QTimer(self)
        self.timer_juego.setSingleShot(True)
        self.timer_juego.timeout.connect(self.terminar_juego)
        #Timer actualiza juego
        self.timer_actualizar_juego = QTimer(self)
        self.timer_actualizar_juego.setInterval(100)
        self.timer_actualizar_juego.timeout.connect(self.actualizar_juego)
        #Timer actualiza barra de tiempo
        self.timer_actualizar_tiempo = QTimer(self)
        self.timer_actualizar_tiempo.setInterval(1000)
        self.timer_actualizar_tiempo.timeout.connect(self.actualizar_tiempo)

    def iniciar_timers(self):
        '''
        Inicializa los timers
        '''
        self.timer_juego.setInterval(p.DURACION_NIVEL_INICIAL * self.ponderador)
        self.recibir_input = True
        self.pausado = False
        self.terminado = False
        self.cheat_ovni = []
        self.cheat_cia = []
        self.descuento_balas = True
        self.tiempo_restante = self.tiempo_restante * self.ponderador

        self.senal_balas.emit(f'{self.balas}')
        self.timer_juego.start()
        self.timer_actualizar_tiempo.start()
        self.timer_actualizar_juego.start()

    def actualizar_juego(self):
        estado = True
        for alien in self.aliens[0]:
            if alien.timer.isActive():
                estado = False
        if estado:
            self.aliens.pop(0)
            if len(self.aliens) <= 0:
                self.terminar_juego()
            else:
                self.aparecer_aliens()
        if self.balas <= 0:
            self.terminar_juego()
            
    def actualizar_tiempo(self):
        self.tiempo_restante -= 1
        self.senal_actualizar_tiempo.emit(self.ponderador)

    def aparecer_aliens(self):
        self.aliens[0][0].aparecer()
        self.aliens[0][1].aparecer()
        self.mover_aliens()

    def mover_aliens(self):
        '''
        Inicializa el movimiento de
        los aliens del par actual
        '''
        self.aliens[0][0].timer.start()
        self.aliens[0][1].timer.start()

    def crear_mira(self):
        '''
        Crea la mira
        '''
        self.mira = Mira()
        self.senal_enviar_mira.emit(self.mira)
        self.mira.label.move(700 /2, 350 / 2)
    
    def nuevo_nivel(self, nivel):
        self.nivel = nivel
        self.crear_mira()
        self.balas = nivel * 4
        self.crear_aliens((self.usuario, self.nivel))
        self.iniciar_timers()

    def mover_mira(self, dir):
        '''
        Ejecuta el movimiento
        de la mira
        '''
        if self.recibir_input:
            self.mira.mover(dir)

    def disparar_mira(self):
        '''
        Ejecuta el disparo
        '''
        if self.recibir_input:
            #Resta de una bala
            if self.descuento_balas:
                self.balas -= 1
            #Se actualiza el numero de balas en al label
            self.senal_balas.emit(f'{self.balas}')
            #Se ejecuta la animacion de la mira
            self.mira.disparar()
            #Se verifica si se ha atinado a un alien
            self.verificar_kill()
    
    def verificar_kill(self):
        '''
        Verifica si le has atinado
        a un alien
        '''
        #Se definen las coordenadas del centro de la mira
        x = self.mira.label.x() + self.mira.label.width() / 2
        y = self.mira.label.y() + self.mira.label.height() / 2
        #Se revisa por cada alien su rectagulo de posición
        for alien in self.aliens[0]:
            tupla = self.rectangulo_alien(alien)
            if tupla[0] <= x <= tupla[2] \
                and tupla[1] <= y <= tupla[3]:
                alien.timer.stop()
                alien.matar()
                self.mira.explosion_inicial()
            del tupla
    
    def rectangulo_alien(self, alien):
        '''
        Calcula el rectángulo
        de posición del alien
        '''
        x_alien = alien.label.x()
        y_alien = alien.label.y()
        ancho_alien = alien.label.width()
        alto_alien = alien.label.height()
        return (x_alien, y_alien, x_alien + ancho_alien, y_alien + alto_alien)

    def chequeo_cheat(self, tecla):
        ovni_cheat = ['O', 'V', 'N', 'I']
        cia_cheat = ['C', 'I', 'A']

        self.cheat_ovni.append(tecla)
        self.cheat_cia.append(tecla)

        if len(self.cheat_ovni) > 4:
            self.cheat_ovni.pop(0)
        if len(self.cheat_cia) > 3:
            self.cheat_cia.pop(0)
        
        if self.cheat_ovni == ovni_cheat:
            self.descuento_balas = False
        elif self.cheat_cia == cia_cheat:
            if self.nivel != 3:
                self.pasar_nivel()

    def pasar_nivel(self):
        puntaje_nivel = self.calcular_puntaje()
        self.puntaje += puntaje_nivel
        self.recibir_input = False
        self.terminado = True
        self.timer_actualizar_juego.stop()
        self.timer_juego.stop()
        self.timer_actualizar_tiempo.stop()
        self.mira.label.setHidden(True)
        self.mira = None

        if len(self.aliens) > 0:
            for alien in self.aliens[0]:
                alien.timer.stop()
                alien.label.setHidden(True)
            
        self.senal_pasar_nivel.emit(self.nivel + 1)
        self.nuevo_nivel(self.nivel + 1)

    def pausar(self):
        if not self.terminado:
            if self.pausado:
                for lista in self.aliens:
                    for alien in lista:
                        alien.timer.start()
                self.timer_actualizar_juego.start()
                self.timer_juego.start()
                self.timer_actualizar_tiempo.start()
                self.pausado = False
                self.recibir_input = True
            else:
                for lista in self.aliens:
                    for alien in lista:
                        alien.timer.stop()
                self.timer_actualizar_juego.stop()
                self.timer_juego.stop()
                self.timer_actualizar_tiempo.stop()
                self.pausado = True
                self.recibir_input = False

    def calcular_puntaje(self):
        if self.nivel == 1:
            ponderador = p.PONDERADOR_TUTORIAL
        elif self.nivel == 2:
            ponderador = p.PONDERADOR_ENTRENAMIENTO
        elif self.nivel == 3:
            ponderador = p.PONDERADOR_INVASION

        puntaje = int((self.nivel * 2 * 100 + \
            (self.tiempo_restante * 30 + self.balas * 70)\
                 * self.nivel) / ponderador)
        return puntaje

    def salir(self):
        puntaje_nivel = self.calcular_puntaje()
        self.puntaje += puntaje_nivel
        escribir(self.usuario, self.puntaje)
        self.hide()

    def terminar_juego(self):
        '''
        Termina el juego
        '''
        puntaje_nivel = self.calcular_puntaje()
        self.puntaje += puntaje_nivel
        self.recibir_input = False
        self.terminado = True
        self.timer_actualizar_juego.stop()
        self.timer_juego.stop()
        self.timer_actualizar_tiempo.stop()
        self.mira.label.setHidden(True)
        self.mira = None

        if len(self.aliens) > 0:
            for alien in self.aliens[0]:
                alien.timer.stop()
                alien.label.setHidden(True)
            status = False
            self.senal_label_termino.emit(0)
        else:
            status = True
            self.senal_label_termino.emit(1)
            self.animacion_terminator()

        self.timer_termino = QTimer()
        self.timer_termino.setInterval(2000)
        self.timer_termino.setSingleShot(True)
        self.timer_termino.timeout.connect(self.enviar_senal_post)
        self.timer_termino.start()

        self.diccionario = {'nivel': self.nivel,
                        'balas': self.balas,
                        'tiempo': self.tiempo_restante,
                        'puntaje_t': self.puntaje,
                        'puntaje_n': puntaje_nivel,
                        'usuario': self.usuario,
                        'status': status}

    def enviar_senal_post(self):
        self.senal_post_juego.emit(self.diccionario)

    def animacion_terminator(self):
        self.senal_animacion_terminator_dog.emit()
        timer_terminator = QTimer()
        timer_terminator.setInterval(1000)
        timer_terminator.setSingleShot(True)
        timer_terminator.timeout.connect(self.resetear_sprite)
    
    def resetear_sprite(self):
        self.senal_reset_sprite.emit()
    

################## LOGICAJUEGO ##################