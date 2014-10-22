#Keyboard input

import pygame


running = True
keys = {
	'w':False,
	'a':False,
	's':False,
	'd':False
}

def update():
	global running
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
                        #quitGame()
                        running = False
                        print "closing down!"
                        
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				keys['w'] = True
			if event.key == pygame.K_a:
				keys['a'] = True
			if event.key == pygame.K_s:
				keys['s'] = True
			if event.key == pygame.K_d:
				keys['d'] = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				keys['w'] = False
			if event.key == pygame.K_a:
				keys['a'] = False
			if event.key == pygame.K_s:
				keys['s'] = False
			if event.key == pygame.K_d:
				keys['d'] = False
			
			
