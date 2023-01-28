from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import parametros as p
from random import randint, choice

################## ALIEN ##################

class Alien(QThread):

    def __init__(self, nivel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nivel = nivel
        self.init_gui()
        self.crear_timer()
    
    def init_gui(self):
        #Definicion de Ponderadores
        ponderadores = [-1, 1]
        #Creacion del label
        self.label = QLabel('')
        self.label.setMaximumSize(75, 75)
        #Definicion del sprite
        if self.nivel == 1:
            pixmap = QPixmap(p.RUTA_ALIEN_LUNA)
            self.muerto = QPixmap(p.RUTA_ALIEN_LUNA_MUERTO)
            ponderador = p.PONDERADOR_TUTORIAL
        elif self.nivel == 2:
            pixmap = QPixmap(p.RUTA_ALIEN_JUPITER)
            self.muerto = QPixmap(p.RUTA_ALIEN_JUPITER_MUERTO)
            ponderador = p.PONDERADOR_ENTRENAMIENTO
        elif self.nivel == 3:
            pixmap = QPixmap(p.RUTA_ALIEN_GALAXIA)
            self.muerto = QPixmap(p.RUTA_ALIEN_GALAXIA_MUERTO)
            ponderador = p.PONDERADOR_INVASION
        #Randomizamos el vector inicial
        self.vector = p.VELOCIDAD_ALIEN.copy()
        self.vector[0] = (self.vector[0] / ponderador) * choice(ponderadores)
        self.vector[1] = (self.vector[1] / ponderador) * choice(ponderadores)
        #Definimos el pixmap del alien
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
    
    def crear_timer(self):
        '''
        Crea el timer de movimiento
        del alien
        '''
        self.timer = QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(self.mover)

        self.timer_muerto = QTimer()
        self.timer_muerto.setInterval(1000)
        self.timer_muerto.setSingleShot(True)
        self.timer_muerto.timeout.connect(self.ocultar)
    
    def aparecer(self):
        '''
        Inicia al alien en una
        posición aleatoria
        '''
        x_max = self.label.parent().width()
        self.label.move(randint(0, x_max), randint(0, p.ALTO_MENU))
        self.label.setVisible(True)

    def mover(self):
        '''
        Mueve al alien
        '''
        #Definicion de posicion final
        x_final = self.label.x() + self.vector[0]
        y_final = self.label.y() + self.vector[1]
        #Chequeo de choque horizontal
        if x_final > self.label.parent().width() - self.label.width():
            x_final = self.label.parent().width() - self.label.width()
            self.vector[0] = self.vector[0] * -1
        elif x_final < 0:
            x_final = 0
            self.vector[0] = self.vector[0] * -1
        #Chequeo de choque vertical
        if y_final > p.ALTO_MENU - self.label.height():
            y_final = p.ALTO_MENU - self.label.height()
            self.vector[1] = self.vector[1] * -1
        elif y_final < 0:
            y_final = 0
            self.vector[1] = self.vector[1] * -1
        #Efectua el movimiento
        self.label.move(x_final, y_final)
    
    def ocultar(self):
        self.label.setVisible(False)

    def matar(self):
        self.label.setPixmap(self.muerto)
        self.timer_muerto.start()
        

################## ALIEN ##################
