from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import parametros as p

class VentanaInicio(QWidget):
    #ventana_inicio.senal_mostrar = ventana_ranking.senal_volver
    senal_ranking = pyqtSignal()
    senal_jugar = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
    
    def init_gui(self):
        '''
        Inicializa los elementos de la interfáz gráfica
        '''
        #Geometria
        self.setGeometry(200, 200, 400, 500)
        self.setFixedSize(400, 500)

        #Titulo Ventana
        self.setWindowTitle('DCComando Espacial')

        #Logo
        self.logo = QLabel(self)
        self.logo.setMaximumSize(450, 230)
        pixmap = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        #Boton Jugar
        self.b_jugar = QPushButton('&Jugar', self)
        self.b_jugar.resize(self.b_jugar.sizeHint())
        self.b_jugar.clicked.connect(self.enviar_jugar)
        h_jugar = QHBoxLayout()
        h_jugar.addSpacing(100)
        h_jugar.addWidget(self.b_jugar)
        h_jugar.addSpacing(100)

        #Boton Ranking
        self.b_rank = QPushButton('&Rankings', self)
        self.b_rank.clicked.connect(self.enviar_rank)
        h_rank = QHBoxLayout()
        h_rank.addSpacing(100)
        h_rank.addWidget(self.b_rank)
        h_rank.addSpacing(100)

        #Layout Vertical
        v_layout = QVBoxLayout()
        v_layout.addStretch(1)
        v_layout.addWidget(self.logo)
        v_layout.addStretch(1.5)
        v_layout.addLayout(h_jugar)
        v_layout.addLayout(h_rank)
        v_layout.addStretch(1)
        self.setLayout(v_layout)

        #Estilizar componentes
        self.estilizar()

        #Mostrar Ventana
        self.mostrar_ventana()
    
    def estilizar(self):
        '''
        Estiliza los elementos de la interfáz gráfica
        '''
        #Color Ventana
        self.setStyleSheet("background-color: #0e1416;"
                            "border: 2px dashed #8ec9db")
        
        #Color de botones
        self.b_jugar.setStyleSheet("background-color: #ffffff;"
                                        "border :2px solid ;"
                                        "border-color: #8ec9db;")
        self.b_rank.setStyleSheet("background-color: #ffffff;"
                                        "border :2px solid ;"
                                        "border-color: #8ec9db;")
    
    def enviar_jugar(self):
        '''
        Envía la señal que abre la ventana principal
        '''
        self.senal_jugar.emit()
        self.hide()
    
    def enviar_rank(self):
        '''
        Envía la señal que abre la ventana de rankings
        '''
        self.senal_ranking.emit()
        self.hide()
    
    def mostrar_ventana(self):
        '''
        Muestra la ventana de inicio
        '''
        self.show()

