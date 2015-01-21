import scoring
import pygame
class GuiHUD(object):


    def __init___(self):
        pass

    def render(self,screen,level,font):
        text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
   	textpos = text.get_rect(center=(60,60))
        screen.blit(text, textpos)


    def tick(self):
        pass
                                     
        

        
