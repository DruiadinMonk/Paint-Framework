# Button class to create button objects in Paint.

# MODULES
import pygame



# BUTTON CLASS
class Button:


	# INTIIALIZE
	def __init__(self, window, color, x, y, w, h):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h


	# DRAW BUTTON & IMAGE: Draw square button and image over it, depending on 'number' value.
	def draw(self, number):

		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h), 1)

		# BUTTON 1: Small 'S'
		if number == 0:
			pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 5)

		# BUTTON 2: Medium 'M'
		if number == 1:
			pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 10)

		# BUTTON 3: Large 'L'
		if number == 2:
			pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 15)

		# BUTTON 4: Circle
		if number == 3:
			pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 15)

		# BUTTON 5: Triangle [(x1, y1), (x2, y2), (x3, y3)]
		if number == 4:
			pygame.draw.polygon(self.window, self.color, [(self.x + 20, self.y + 5), (self.x + 35, self.y + 35), (self.x + 5, self.y + 35)])

		# BUTTON 6: Square
		if number == 5:
			pygame.draw.rect(self.window, self.color, (self.x + 5, self.y + 5, 30, 30))

		# BUTTON 7: White
		if number == 6:
			pygame.draw.rect(self.window, (255, 255, 255), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 8: Black
		if number == 7:
			pygame.draw.rect(self.window, (  0,   0,   0), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 9: Red
		if number == 8:
			pygame.draw.rect(self.window, (255,   0,   0), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 10: Orange
		if number == 9:
			pygame.draw.rect(self.window, (255, 165,   0), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 11: Yellow
		if number == 10:
			pygame.draw.rect(self.window, (255, 255,   0), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 12: Green
		if number == 11:
			pygame.draw.rect(self.window, (  0, 255,   0), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 13: BLue
		if number == 12:
			pygame.draw.rect(self.window, (  0,   0, 255), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 14: Purple
		if number == 13:
			pygame.draw.rect(self.window, (143,   0, 255), (self.x + 1, self.y + 1, 38, 38))

		# BUTTON 15: Erase ALL, with a big 'X'.
		if number == 14:
			pygame.draw.line(self.window, (255,   0,   0), (self.x + 3, self.y +  3), (self.x + 37, self.y + 37), 3)
			pygame.draw.line(self.window, (255,   0,   0), (self.x + 3, self.y + 37), (self.x + 37, self.y +  3), 3)
