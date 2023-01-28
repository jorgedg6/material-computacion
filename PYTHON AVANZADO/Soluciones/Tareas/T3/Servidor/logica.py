"""
Modulo contiene la clase Logica del servidor
"""

from utils import data_json
from os.path import join


class Logica:
    def __init__(self, parent):
        # Esto permite ejecutar funciones de la clase Servidor
        self.parent = parent