import os
from random import uniform

RUTA_LOGO = os.path.join('Sprites', 'Logo', 'Logo.png')
RUTA_PUNTAJES = os.path.join('puntajes.txt')

RUTA_FONDO_LUNA = os.path.join('Sprites', 'Fondos', 'Luna.png')
RUTA_ALIEN_LUNA = os.path.join('Sprites', 'Aliens', 'Alien1.png')
RUTA_ALIEN_LUNA_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien1_dead.png')

RUTA_FONDO_JUPITER = os.path.join('Sprites', 'Fondos', 'Jupiter.png')
RUTA_ALIEN_JUPITER = os.path.join('Sprites', 'Aliens', 'Alien2.png')
RUTA_ALIEN_JUPITER_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien2_dead.png')

RUTA_FONDO_GALAXIA = os.path.join('Sprites', 'Fondos', 'Galaxia.png')
RUTA_ALIEN_GALAXIA = os.path.join('Sprites', 'Aliens', 'Alien3.png')
RUTA_ALIEN_GALAXIA_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien3_dead.png')

RUTA_UI_PRINCIPAL = os.path.join('UI', 'PRINCIPAL.ui')
RUTA_UI_JUEGO = os.path.join('UI', 'JUEGO.ui')
RUTA_UI_POST_JUEGO = os.path.join('UI', 'POST_JUEGO.ui')

RUTA_BALA = os.path.join('Sprites', 'Elementos juego', 'Bala.png')
RUTA_DISPARADOR = os.path.join('Sprites', 'Elementos juego', 'Disparador_negro.png')
RUTA_DISPARADOR_ROJO = os.path.join('Sprites', 'Elementos juego', 'Disparador_rojo.png')

RUTA_SONIDO_DISPARADOR = os.path.join('Sonidos', 'disparo.wav')
RUTA_SONIDO_TERMINATOR = os.path.join('Sonidos', 'risa_robotica.wav')

RUTA_EXPLOSION_INICIAL = os.path.join('Sprites', 'Elementos juego', 'Disparo_f1.png')
RUTA_EXPLOSION_MEDIA = os.path.join('Sprites', 'Elementos juego', 'Disparo_f2.png')
RUTA_EXPLOSION_FINAL = os.path.join('Sprites', 'Elementos juego', 'Disparo_f3.png')

RUTA_TERMINATOR_DOG = os.path.join('Sprites', 'Terminator-Dog', 'Dog1.png')

RUTA_TERMINATOR_DOG_ALIEN_LUNA = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien1.png')
RUTA_TERMINATOR_DOG_ALIEN_JUPITER = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien2.png')
RUTA_TERMINATOR_DOG_ALIEN_GALAXIA = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien3.png')

TECLA_ARRIBA = 'W'
TECLA_IZQUIERDA = 'A'
TECLA_DERECHA = 'D'
TECLA_ABAJO = 'S'
TECLA_DISPARO = 'F'

CANTIDAD_ALIENS_LUNA = 2
CANTIDAD_ALIENS_JUPITER = 6
CANTIDAD_ALIENS_GALAXIA = 8

MOVIMIENTO_MIRA = 10

VELOCIDAD_ALIEN = [1, 1]

PONDERADOR_TUTORIAL = uniform(0.9, 1.0)
PONDERADOR_ENTRENAMIENTO = uniform(0.8, 0.9)
PONDERADOR_INVASION = uniform(0.7, 0.8)

ALTO_MENU = 450

DURACION_NIVEL_INICIAL = 60000
ACTUALIZAR_JUEGO = 100
ACTUALIZAR_ALIEN = 100