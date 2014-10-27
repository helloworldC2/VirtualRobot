#Keyboard input

import pygame
import Tile


running = True
keys = {
	'w':False,
	'a':False,
	's':False,
	'd':False,
        'h':False,
        'e':False,
        'l':False,
        'o':False
}
cheatOn = False
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
			if event.key == pygame.K_o:
				keys['o'] = True
			if event.key == pygame.K_h:
				keys['h'] = True
			if event.key == pygame.K_l:
				keys['l'] = True
			if event.key == pygame.K_e:
				keys['e'] = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				keys['w'] = False
			if event.key == pygame.K_a:
				keys['a'] = False
			if event.key == pygame.K_s:
				keys['s'] = False
			if event.key == pygame.K_d:
				keys['d'] = False
			if event.key == pygame.K_o:
				keys['o'] = False
			if event.key == pygame.K_h:
				keys['h'] = False
			if event.key == pygame.K_l:
				keys['l'] = False
			if event.key == pygame.K_e:
				keys['e'] = False

                isCheatOn()
                
def isCheatOn():
        global cheatOn,keys
        if keys['h'] and keys['e'] and keys['l'] and keys['o']:
                cheatOn = not cheatOn
                Tile.tiles[3].setSolid(not cheatOn)
                print 'CHEAT TOGGLED'
        
			
			
