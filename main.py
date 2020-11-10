# Simple Paint program

# MODULES
import pygame
import sys
from button import Button



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 640, 600
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
run = True
FPS = 60



# COLORS
WHITE 	= (255, 255, 255)
BLACK 	= (  0,   0,   0)
L_GRAY 	= (170, 170, 170)
D_GRAY 	= ( 85,  85,  85)
RED 	= (255,   0,   0)
ORANGE 	= (255, 165,   0)
YELLOW 	= (255, 255,   0)
GREEN 	= (  0, 255,   0)
BLUE 	= (  0,   0, 255)
PURPLE 	= (143,   0, 255)



# INITIALIZE OBJECTS
buttons = [] 	# 6 Colors, 3 shapes, 3 size of brush.
x = y = 0 		# Starting point of 1st button.
w = h = 25 		# Size of button.

for i in range(15):

	b = Button(window, L_GRAY, x, y, 40, 40)
	buttons.append(b)

	y += 40



# MAIN LOOP
while run:

	# INITIALIZE
	clock.tick(FPS) 			# Speed of game
	window.fill(BLACK) 	
	# keys = pygame.key.get_pressed()
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()

	# EACH EVENT
	for event in pygame.event.get():

		# IF QUIT...
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()










	# DRAW OBJECTS: 'i' is synced up with ALL button images, as all have a unique image to display.
	for i in range(len(buttons)):
		buttons[i].draw(i)


	# UPDATE
	pygame.display.update()
