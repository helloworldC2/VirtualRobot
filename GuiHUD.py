import scoring
import pygame
import gui
import Game
class GuiHUD(object):


    def __init__(self):
        self.time = 1

    def render(self,screen,level,font):
        if gui.gameOver==True:
            font = pygame.font.SysFont(None, 128)
            text = font.render("GAME OVER!", True, (0,0,0))
            textpos = text.get_rect(center=(400,300))
            screen.blit(text, textpos)
            for e in level.entities:
                try:
                    if e.score.score >= level.player.score.score:
                            font = pygame.font.SysFont(None, 64)
                            text = font.render("AI WINS", True, (0,0,0))
                            textpos = text.get_rect(center=(400,420))
                            screen.blit(text, textpos)
                            return
                except:
                    pass
            font = pygame.font.SysFont(None, 64)
            text = font.render("YOU WIN!", True, (0,0,0))
            textpos = text.get_rect(center=(400,420))
            screen.blit(text, textpos)
                        
        else:
            text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
            textpos = text.get_rect(center=(60,60))
            screen.blit(text, textpos)
            y = 60
            for e in level.entities:
                try:
                    if e.score !=None:
                        y=y+30
                        text = font.render("AI: "+str(e.score.score), True, (0,0,0))
                        textpos = text.get_rect(center=(500,y))
                        screen.blit(text, textpos)
                except:
                    pass
                
            if gui.isMultiplayer==False:
                text = font.render("Time: "+str(100-self.time), True, (0,0,0))
                textpos = text.get_rect(center=(60,100))
                screen.blit(text, textpos)
                text2 = font.render("Health bar:", True, (0,0,0))
                textpos2 = text.get_rect(center=(60,150))
                screen.blit(text2, textpos2)
        if gui.defeat==True:
            font = pygame.font.SysFont(None, 64)
            text1 = font.render("You Lose!", True, (0,0,0))
            textpos1 = text.get_rect(center=(400,300))
            screen.blit(text1, textpos1)



    def tick(self,ticks):
        self.time = ticks/60
        if gui.gameOver==True or gui.defeat==True:
            if pygame.mouse.get_pressed()[0]==True:
                gui.gameOver=False
                gui.scorePosted = False
                Game.menu1(gui.screen)
        
                                     
        

        
