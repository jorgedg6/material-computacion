from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal

import lectura as l
import parametros as p

class VentanaRankings(QWidget):
    
    senal_volver = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.puntajes = l.leer(p.RUTA_PUNTAJES)
        self.init_gui()
    
    def init_gui(self):
        '''
        Inicializa los elementos de la interfáz gráfica
        '''
        #VENTANA
        #Geometria
        self.setGeometry(200, 200, 400, 500)
        self.setFixedSize(400, 500)
        #Color
        self.setStyleSheet("background-color: #0e1416")
        #Titulo
        self.setWindowTitle('Rankings')

        #Layout Vertical
        v_layout = QVBoxLayout()

        #Titulo
        self.titulo = QLabel('RANKING DE PUNTAJES', self)
        self.titulo.setFont(QFont('Arial', 30))
        self.titulo.setStyleSheet("color: #8ec9db;"
                                  "font-weight: bold")
        h_titulo = QHBoxLayout()
        h_titulo.addStretch(1)
        h_titulo.addWidget(self.titulo)
        h_titulo.addStretch(1)
        v_layout.addLayout(h_titulo)

        for i in range(5):
            usuario, puntaje = self.puntajes[i]
            label_u = QLabel(f'{i+1}.  {usuario}')
            label_u.setStyleSheet("color: white;"
                                  "font-weight: bold")
            label_p = QLabel(f'{puntaje}')
            label_p.setStyleSheet("color: white;"
                                  "font-weight: bold")
            h_label = QHBoxLayout()
            h_label.addSpacing(50)
            h_label.addWidget(label_u)
            h_label.addStretch(1)
            h_label.addWidget(label_p)
            h_label.addSpacing(50)
            v_layout.addLayout(h_label)
        
        #Boton
        self.boton = QPushButton('&Volver', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.volver)
        self.boton.setStyleSheet("background-color: #ffffff;"
                                "border :2px solid ;"
                                "border-color: #8ec9db;")
        v_layout.addWidget(self.boton)

        #Seteo de Layout
        self.setLayout(v_layout)

    def volver(self):
        '''
        Muestra la ventana de inicio y cierra la de ranking
        al presionar el botón
        '''
        self.senal_volver.emit()
        self.hide()
    
    def closeEvent(self, event):
        '''
        Muestra la ventana de inicio y cierra la de ranking
        al cerrar la pestaña
        '''
        event.accept()
        self.senal_volver.emit()
        self.hide()

    def mostrar_ventana(self):
        '''
        Muestra la ventana de ranking
        '''
        self.show()
