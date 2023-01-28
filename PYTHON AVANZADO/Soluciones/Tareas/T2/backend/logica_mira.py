from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QLabel
import parametros as p
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound
from time import sleep

################## MIRA ##################

class Mira(QThread):

    senal_disparo = pyqtSignal(tuple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.negro = QPixmap(p.RUTA_DISPARADOR)
        self.rojo = QPixmap(p.RUTA_DISPARADOR_ROJO)
        self.sonido = QSound(p.RUTA_SONIDO_DISPARADOR)
        self.init_gui()
        self.crear_explosiones()
        self.crear_timers()

    def init_gui(self):
        self.label = QLabel('')
        self.label.setMaximumSize(120, 80)

        self.label_exp = QLabel('')
        self.label_exp.setMaximumSize(80, 80)

        self.color_negro()
    
    def crear_timers(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.color_negro)

        self.timer_exp_inicial = QTimer()
        self.timer_exp_inicial.setInterval(250)
        self.timer_exp_inicial.setSingleShot(True)

        self.timer_exp_media = QTimer()
        self.timer_exp_media.setInterval(250)
        self.timer_exp_media.setSingleShot(True)

        self.timer_exp_final = QTimer()
        self.timer_exp_final.setInterval(250)
        self.timer_exp_final.setSingleShot(True)
    
    def crear_explosiones(self):
        self.exp_inicial = QPixmap(p.RUTA_EXPLOSION_INICIAL)
        self.exp_media = QPixmap(p.RUTA_EXPLOSION_MEDIA)
        self.exp_final = QPixmap(p.RUTA_EXPLOSION_FINAL)
    
    def mover(self, dir):
        '''
        Procesa el movimiento de la mira
        '''
        x_final = self.label.x()
        y_final = self.label.y()

        if dir == 'U':
            y_final -= p.MOVIMIENTO_MIRA
        elif dir == 'L':
            x_final -= p.MOVIMIENTO_MIRA
        elif dir == 'R':
            x_final += p.MOVIMIENTO_MIRA
        elif dir == 'D':
            y_final += p.MOVIMIENTO_MIRA
        
        if x_final > self.label.parent().width() - self.label.width():
            x_final = self.label.parent().width() - self.label.width()
        elif x_final < 0:
            x_final = 0
        if y_final > p.ALTO_MENU - self.label.height():
            y_final = p.ALTO_MENU - self.label.height()
        elif y_final < 0:
            y_final = 0
        
        self.label.move(x_final, y_final)
    
    def color_negro(self):
        '''
        Establece la mira color negro
        '''
        self.label.setPixmap(self.negro)
        self.label.setScaledContents(True)

    def color_rojo(self):
        '''
        Establece la mira colo roja
        '''
        self.label.setPixmap(self.rojo)
        self.label.setScaledContents(True)

    def disparar(self):
        '''
        Efectúa el cambio de color de mira
        '''
        self.color_rojo()
        self.sonido.play()
        self.timer.start()
    
    def explosion_inicial(self):
        x = self.label.x()
        y = self.label.y()

        self.label_exp.move(x, y)
        self.label_exp.setPixmap(self.exp_inicial)
        self.label_exp.setScaledContents(True)
        self.label_exp.setVisible(True)
        self.label_exp.raise_()

        self.timer_exp_media.timeout.connect(self.explosion_media)
        self.timer_exp_media.start()
        pass

    def explosion_media(self):
        self.label_exp.setPixmap(self.exp_media)
        self.label_exp.setScaledContents(True)
        self.timer_exp_final.timeout.connect(self.explosion_final)
        self.timer_exp_final.start()
    
    def explosion_final(self):
        self.label_exp.setPixmap(self.exp_final)
        self.label_exp.setScaledContents(True)
        self.timer_exp_inicial.timeout.connect(self.ocultar_explosion)
        self.timer_exp_inicial.start()
    
    def ocultar_explosion(self):
        self.label_exp.setVisible(False)
        self.timer_exp_inicial.stop()
    
################## MIRA ##################


