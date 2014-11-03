import pygame

pygame.init()

x,y=0,0

moveX=0
moveY=0

clock=pygame.time.Clock()
gameLoop=True 
while gameLoop:
    
    for event in pygame.event.get():
        
        if(event.type==pygame.QUIT):

            gameLoop=False

        if (event.type==pygame.KEYDOWN):

            if (event.key==pygame.K_LEFT):
                moveX=-5

            if (event.key==pygame.K_RIGHT):
                moveX=5

            if (event.key==pygame.K_UP):
                moveY=-5

            if (event.key==pygame.K_DOWN):
                moveY=5


        if (event.type==pygame.KEYUP):

            if (event.key==pygame.K_LEFT):
                moveX=-0

            if (event.key==pygame.K_RIGHT):
                moveX=0

            if (event.key==pygame.K_UP):
                moveY=-0

            if (event.key==pygame.K_DOWN):
                moveY=0
                
 
    x+=moveX
    y+=moveY


    clock.tick(50)

    pygame.display.flip()

pygame.quit()
