import scoring
import pygame
import gui
class GuiHUD(object):


    def __init__(self):
        self.time = 1

    def render(self,screen,level,font):
        if gui.gameOver==True:
            font = pygame.font.SysFont(None, 128)
            text = font.render("GAME OVER!", True, (0,0,0))
            textpos = text.get_rect(center=(60,160))
            screen.blit(text, textpos)
        else:
            text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
            textpos = text.get_rect(center=(60,60))
            screen.blit(text, textpos)
            if gui.isMultiplayer==False:
                text = font.render("Time: "+str(100-self.time), True, (0,0,0))
                textpos = text.get_rect(center=(400,300))
                screen.blit(text, textpos)

    def tick(self,ticks):
        self.time = ticks/60
        
                                     
        

        
