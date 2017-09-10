import pygame

screen = pygame.display.set_mode((320, 200))


running = 1

while running:
	
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((135,206,250))
	pygame.display.flip()