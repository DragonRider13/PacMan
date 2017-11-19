import pygame
from pygame.locals import *
from PacMan2 import PacMan2
from Tile import Tile

#screen = pygame.display.set_mode((200, 200))

pygame.init()
SCREENSIZE = (600,400)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
clock = pygame.time.Clock()
x,y = (300,200)
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill((0,0,0))
pacman = PacMan2((50,50), [500,200])
tile = Tile((150,150), [150,100])

running = 1

while running:
	time_passed = clock.tick(30)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			running = 0
	pacman.move()
	pacman.collide(tile)
	screen.blit(background, (0, 0))
	tile.draw(screen)
	pacman.draw(screen)
	#pacman.render(screen)
	pygame.display.update()
	
	#event = pygame.event.poll()
	#if event.type == pygame.QUIT:
	#	running = 0
	#screen.fill((51,255,255))
	#blue = 0,0,255
	#white = 255,255,255
	#point1 = 0,200
	#point2 = 200,0
	#pygame.draw.line(screen, white, point1, point2)
	#x = 10
	#while x < 201:
	#	pygame.draw.line (screen,white,(x%10,200-x), (x,0))
	#	x = x + 10
	#x = 10
	#while x < 201:
	#	pygame.draw.line (screen, blue, (0, x),(200-x,x%10))
	#	x = x + 10
	#pygame.display.flip()
