from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtMultimedia import QSound
import parametros as p
from PyQt5 import uic
from random import randint
from lectura import escribir

window_name, base_class = uic.loadUiType(p.RUTA_UI_JUEGO)

class VentanaJuego(window_name, base_class):

    senal_tecla = pyqtSignal(str)
    senal_disparo = pyqtSignal()
    senal_pausa = pyqtSignal()
    senal_cheat = pyqtSignal(str)
    senal_salir = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.valor_barra = 100
        self.tiempo_restante = p.DURACION_NIVEL_INICIAL / 1000
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.risa_terminator = QSound(p.RUTA_SONIDO_TERMINATOR)
    
    def init_gui(self):
        '''
        Inicializa los elementos
        de la interfáz gráfica
        '''
        #Seleccionamos fondo y título según nivel seleccionado
        if self.nivel == 1:
            pixmap_fondo = QPixmap(p.RUTA_FONDO_LUNA)
            self.setWindowTitle(f'Tutorial Lunar - {self.usuario}')
            self.nivel = 1
        elif self.nivel == 2:
            pixmap_fondo = QPixmap(p.RUTA_FONDO_JUPITER)
            self.setWindowTitle(f'Entrenamiento en Júpiter - {self.usuario}')
            self.nivel = 2
        elif self.nivel == 3:
            pixmap_fondo = QPixmap(p.RUTA_FONDO_GALAXIA)
            self.setWindowTitle(f'Invasión Intergaláctica - {self.usuario}')
            self.nivel = 3
        #Seteamos el fondo
        self.fondo.setPixmap(pixmap_fondo)
        self.fondo.setScaledContents(True)
        #Seteamos terminator dog
        self.pixmap_terminator = QPixmap(p.RUTA_TERMINATOR_DOG)
        self.label_terminator.setPixmap(self.pixmap_terminator)
        self.label_terminator.setScaledContents(True)
        #Barra Tiempo
        self.valor_barra = 100
        self.barra_tiempo.setValue(self.valor_barra)
        self.barra_tiempo.setTextVisible(False)
        #Cambiamos el label de nivel
        self.label_nivel.setText(str(self.nivel))
        #Reseteamos el label de termino
        self.label_termino.setText('')
        #Conectamos botones
        self.b_pausa.clicked.connect(self.pausar)
        self.b_salir.clicked.connect(self.salir)
        #Mostramos la ventana
        self.show()
        pass
    
    def cambiar_puntaje(self, puntaje):
        self.puntos.setText(f'{puntaje} ptos')

    def mostrar_ventana(self, tupla):
        '''
        Muestra la ventana
        '''
        self.usuario = tupla[0]
        self.nivel = tupla[1]
        self.init_gui()
    
    def nuevo_nivel(self, nivel):
        self.nivel = nivel
        self.init_gui()

    def conectar_aliens(self, lista):
        '''
        Conecta los aliens
        a la ventana
        '''
        self.aliens = lista
        for par in self.aliens:
            for alien in par:
                alien.label.setParent(self)

    def keyPressEvent(self, event):
        '''
        Envía la señal de la tecla al backend
        '''
        tecla = event.text().upper()
        if tecla == p.TECLA_DISPARO:
            self.senal_disparo.emit()
        elif tecla == 'P':
            self.senal_pausa.emit()
        else:
            if tecla == p.TECLA_ARRIBA:
                self.senal_tecla.emit('U')
            elif tecla == p.TECLA_IZQUIERDA:
                self.senal_tecla.emit('L')
            elif tecla == p.TECLA_DERECHA:
                self.senal_tecla.emit('R')
            elif tecla == p.TECLA_ABAJO:
                self.senal_tecla.emit('D')
        self.senal_cheat.emit(tecla)

    def conectar_mira(self, mira):
        '''
        Conecta la mira a la ventana
        '''
        #Se conecta la mira
        self.mira = mira
        self.mira.label.setParent(self)
        self.mira.label.setVisible(True)
        #Se conecta la explosion
        self.mira.label_exp.setParent(self)
    
    def actualizar_balas(self, balas):
        self.balas.setText(balas)
    
    def actualizar_tiempo(self, ponderador):
        '''
        Actualiza la barra de tiempo
        '''
        self.tiempo_restante -= 1
        self.valor_barra -= 100 / ((p.DURACION_NIVEL_INICIAL * ponderador) / 1000)
        if self.valor_barra >= 0:
            self.barra_tiempo.setValue(self.valor_barra)
            self.barra_tiempo.update()
        pass

    def actualizar_label_termino(self, num):
        if num == 0:
            self.label_termino.setText('QUE LASTIMA, HAS PERDIDO')
        elif num == 1:
            self.label_termino.setText('¡NIVEL SUPERADO!')
    
    def animacion_terminator_dog(self):
        if self.nivel == 1:
            pixmap = QPixmap(p.RUTA_TERMINATOR_DOG_ALIEN_LUNA)
        elif self.nivel == 2:
            pixmap = QPixmap(p.RUTA_TERMINATOR_DOG_ALIEN_JUPITER)
        elif self.nivel == 3:
            pixmap = QPixmap(p.RUTA_TERMINATOR_DOG_ALIEN_GALAXIA)
        self.label_terminator.setPixmap(pixmap)
        self.label_terminator.setScaledContents(True)
        self.risa_terminator.play()

    def reset_terminator_dog(self):
        self.label_terminator.setPixmap(self.pixmap_terminator)
        self.label_terminator.setScaledContents(True)

    def pausar(self):
        '''
        Envía señal de pausa
        '''
        self.senal_pausa.emit()

    def salir(self):
        self.senal_salir.emit()
        self.cerrar_ventana()

    def cerrar_ventana(self):
        '''
        Cierra la ventana
        del formato actual
        '''
        self.hide()