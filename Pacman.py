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
		xcollide = False
		ycollide = False
		xycollide = False
		x2 = 50
		y2 = 50
		width2 = 150
		height2 = 100
		x = self.position.x
		y = self.position.y
		width = 16
		height = 16
		xcollide = False
		ycollide = False
		xycollide = False
		if x < x2:
		    if x2+width2-x < width+width2:
		        xcollide = True
		elif x > x2:
		    if x+width-x2 < width+width2:
		        xcollide = True
		elif x == x2:
		    xcollide = True

		if xcollide:
		    if y < y2:
		        if y2+height2-y < height+height2:
		            ycollide = True
		    elif y > y2:
		        if y+height-y2 < height+height2:
		            ycollide = True
		    elif y == y2:
		        ycollide = True

		xycollide = xcollide & ycollide
		if xycollide:
		    pygame.draw.rect(screen, (100,100,100),[x2,y2,width2,height2])
		else:
		    pygame.draw.rect(screen, (255,0,0),[x2,y2,width2,height2])
		pygame.draw.rect(screen, (0,0,255),[400,300,60,80])
		pygame.draw.circle(screen, (255,255,0), self.position.toTuple(),16)
