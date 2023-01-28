import pygame
import random

from pygame.locals import(
	K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL)

# ahora el objeto Surface que habíamos dibujado en la pantalla principal es un atributo de Player
# heredamos añadiendolo como parámetro a la clase Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
		# nos permite invocar métodos o atributos de Sprite
	    super(Player, self).__init__()
	    self.surf = pygame.image.load("/Users/jorgedegoyeneche/Downloads/Sprites/profe_Jorge.png")
	    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
	    self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
	    if pressed_keys[K_UP]:
		    self.rect.move_ip(0, -5)
	    if pressed_keys[K_DOWN]:
		    self.rect.move_ip(0, 5)
	    if pressed_keys[K_LEFT]:
		    self.rect.move_ip(-5, 0)
	    if pressed_keys[K_RIGHT]:
		    self.rect.move_ip(5, 0)
        
        # mantener al jugador en pantalla
	    if self.rect.left < 0:
		    self.rect.left = 0
	    if self.rect.right > SCREEN_WIDTH:
		    self.rect.right = SCREEN_WIDTH
	    if self.rect.top < 0:
		    self.rect.top = 0
	    if self.rect.bottom > SCREEN_HEIGHT:
		    self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		self.surf = pygame.image.load("/Users/jorgedegoyeneche/Downloads/Sprites/papitas.png").convert()
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect(
			center = (
								random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
								random.randint(0, SCREEN_HEIGHT),
			)
		)
		self.speed = random.randint(5, 10)
	
	# el sprite tendra velocidad
	# cuando traspase el lado izq de la pantalla lo eliminamos
	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()

class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super(Cloud, self).__init__()
		self.surf = pygame.image.load("/Users/jorgedegoyeneche/Downloads/Sprites/cloud.png").convert()
		self.surf.set_colorkey((255,255,255), RLEACCEL)
		# posicion inicial random
		self.rect = self.surf.get_rect(
			center = (
								random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
								random.randint(0, SCREEN_HEIGHT),
			)
		)

	# igual que los enemigos
	def update(self):
		self.rect.move_ip(-5, 0)
		if self.rect.right < 0:
			self.kill()

pygame.init()

# definir el tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# crear el objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("/Users/jorgedegoyeneche/Downloads/Sprites/san_joaquin.jpg").convert()

# evento para crear enemigos cada cierto intervalo de tiempo
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 350)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# instanciamos al jugador
player = Player()

# creamos grupos para tener a los enemigos y todos los sprites
# cloud para las nubes
# enemies es para detectar colisiones y actualizar posiciones
# all_sprites es para renderizar
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

# variable booleana para manejar el loop
running = True

# loop principal del juego
while running:
	# iteramos sobre cada evento en la cola
    for event in pygame.event.get():
		# se presiono una tecla?
	    if event.type == KEYDOWN:
			# era la tecla de escape? -> entonces terminamos
		    if event.key == K_ESCAPE:
			    running = False

		# fue un click al cierre de la ventana? -> entonces terminamos
	    elif event.type == QUIT:
		    running = False
        
        # es un evento que agrega enemigos?
	    elif event.type == ADDENEMY:
		    new_enemy = Enemy()
		    enemies.add(new_enemy)
		    all_sprites.add(new_enemy)
		
		# es un evento que agrega nubes?
	    elif event.type == ADDCLOUD:
		    new_cloud = Cloud()
		    clouds.add(new_cloud)
		    all_sprites.add(new_cloud)

	# rellena la screen con un color, en este caso blanco
    screen.blit(background_image, [0, 0])

    # dibujamos todos los sprites
    for entity in all_sprites:
	    screen.blit(entity.surf, entity.rect)

    # vemos si algun enemigo a chocado con el jugador
    if pygame.sprite.spritecollideany(player, enemies):
		# si pasa, removemos al jugador y detenemos el loop del juego
	    player.kill()
	    running = False

    pygame.display.flip()
    clock.tick(40)
    # obtenemos todas las teclas presionadas actualmente
    pressed_keys = pygame.key.get_pressed()

    # actualizamos el sprite del jugador basado en las teclas presionadas
    player.update(pressed_keys)

	#Actualizamos los enemigos
    enemies.update()
	#Actualizamos las nubes
    clouds.update()