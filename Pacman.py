import pygame
from pygame.locals import *
from vectors import Vector2D

class Pacman(object):

	def __init__(self, position):
		self.position = Vector2D(position)

	def move(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[K_UP]:
			self.position.y = self.position.y -3
		elif key_pressed[K_DOWN]:
			self.position.y = self.position.y +3
		elif key_pressed[K_LEFT]:
			self.position.x = self.position.x -3
		elif key_pressed[K_RIGHT]:
			self.position.x = self.position.x +3
			
	def render(self, screen):
		pygame.draw.circle(screen, (255,255,0), self.position.toTuple(),16)