import pygame
from pygame.locals import *
from vectors import Vector2D

class Pacman(object):

	#xcollide = axis_overlap(x, width, x2, width2)
	#ycollide = axis_overlap(y, height, y2, height2)
	#xycollide = xcollide & ycollide
	

	def __init__(self, position):
		self.position = Vector2D(position)
		self.direction = 'LEFT'

	def move(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[K_UP]:
			self.position.y = self.position.y -3
			self.direction = 'UP'
		elif key_pressed[K_DOWN]:
			self.position.y = self.position.y +3
			self.direction = 'DOWN'
		elif key_pressed[K_LEFT]:
			self.position.x = self.position.x -3
			self.direction = 'LEFT'
		elif key_pressed[K_RIGHT]:
			self.position.x = self.position.x +3
			self.direction = 'RIGHT'

	def axis_overlap(self, p1, length1, p2, length2):
    		collided = False
    		if p1 < p2:
        		if p2+length2-p1 < length1+length2:
            			collided = True
    		elif p1 > p2:
        		if p1+length1-p2 < length1+length2:
            			collided = True
    		elif p1 == p2:
        		collided = True
    		return collided
			
	def render(self, screen):
		
		xRed = 50
		yRed = 50
		widthRed = 150
		heightRed = 100
		xBlue = 400
		yBlue = 300
		widthBlue = 60
		heightBlue = 80
		x = self.position.x
		y = self.position.y
		width = 16
		height = 16
		if self.direction == 'LEFT':
			xCollideRed = self.axis_overlap(xRed, widthRed, x-16, 16)
		else:
			xCollideRed = self.axis_overlap(xRed, widthRed, x, 16)
		if self.direction == 'UP':
			yCollideRed = self.axis_overlap(yRed, heightRed, y-16, 16)
		else:
			yCollideRed = self.axis_overlap(yRed, heightRed, y, 16) 
		xCollideBlue = self.axis_overlap(xBlue, widthBlue, x, 16)
		yCollideBlue = self.axis_overlap(yBlue, heightBlue, y, 16)
	


		if xCollideRed and yCollideRed:
		    #pygame.draw.rect(screen, (100,100,100),[xRed,yRed,widthRed,heightRed])
			if self.direction is 'UP':
           			self.position.y = yRed+heightRed+width
        		elif self.direction is 'DOWN':
          			self.position.y = yRed-height
        		elif self.direction is 'LEFT':
            			self.position.x = xRed+widthRed+width
        		elif self.direction is 'RIGHT':
            			self.position.x = xRed-width
		
		pygame.draw.rect(screen, (255,0,0),[xRed,yRed,widthRed,heightRed])
		#if xCollideBlue and yCollideBlue:
		#	pygame.draw.rect(screen, (100,100,100),[xBlue,yBlue,widthBlue,heightBlue])
		#else:
		#	pygame.draw.rect(screen, (0,0,225),[xBlue,yBlue,widthBlue,heightBlue])
		
		pygame.draw.circle(screen, (255,255,0), self.position.toTuple(),16)
