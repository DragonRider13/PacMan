import pygame

screen = pygame.display.set_mode((200, 200))


running = 1

while running:
	
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((51,255,255))
	blue = 0,0,255
	white = 255,255,255
	point1 = 0,200
	point2 = 200,0
	#pygame.draw.line(screen, white, point1, point2)
	x = 10
	while x < 201:
		pygame.draw.line (screen,white,(x%10,200-x), (x,0))
		x = x + 10
	x = 10
	while x < 201:
		pygame.draw.line (screen, blue, (0, x),(200-x,x%10))
		x = x + 10
	pygame.display.flip()
