import scoring
import pygame
import gui
import Game
import selectBar
from selectBar import *
import Level
from Level import *
import Tile



class GuiHUD(object):


    def __init__(self,screen,):
        self.time = 1
        self.t1 = image(screen,(30,500),"tiles/brokenChest.png")
        self.t1.scale(32,32)
        self.t2 = image(screen,(80,500),"tiles/burntChest.png")
        self.t2.scale(32,32)
        self.t3 = image(screen,(130,500),"tiles/darkChest.png")
        self.t3.scale(32,32)
        self.t4 = image(screen,(180,500),"tiles/glassChest.png")
        self.t4.scale(32,32)
        self.t5 = image(screen,(230,500),"tiles/goldChest.png")
        self.t5.scale(32,32)
        self.t6 = image(screen,(280,500),"tiles/normalChest.png")
        self.t6.scale(32,32)
        self.t7 = image(screen,(330,500),"tiles/OverFlowChest.png")
        self.t7.scale(32,32)
        self.t8 = image(screen,(380,500),"tiles/crystalChest.png")
        self.t8.scale(32,32)
        self.t9 = image(screen,(430,500),"tiles/sandT.png")
        self.t9.scale(32,32)
        self.t10 = image(screen,(480,500),"tiles/grownOverChest.png")
        self.t10.scale(32,32)

        self.c1 = image(screen,(30,500),"tiles/brokenChest.png")
        self.c1.scale(32,32)
        self.c2 = image(screen,(80,500),"tiles/burntChest.png")
        self.c2.scale(32,32)
        
    def render(self,screen,level,font,x,y):
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
                            textpos = text.get_rect(center=(450,420))
                            screen.blit(text, textpos)
                            return
                except:
                    pass
            if gui.defeat == False:
                font = pygame.font.SysFont(None, 64)
                text = font.render("YOU WIN!", True, (0,0,0))
                textpos = text.get_rect(center=(400,420))
                screen.blit(text, textpos)
            else:
                font = pygame.font.SysFont(None, 64)
                text1 = font.render("You Lose!", True, (0,0,0))
                textpos1 = text.get_rect(center=(577.231,420)) 
                screen.blit(text1, textpos1)
                 
                        
        else:
            if level.player!=None:
                pygame.draw.rect(screen,(255,0,0),(10,170,110,10))
                pygame.draw.rect(screen,(0,255,0),(10,170,level.player.health,10))
                text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
                textpos = text.get_rect(center=(60,60))
                screen.blit(text, textpos)

            if level.player == None:
                ##############
                self.t1.blit()
                self.t2.blit()
                pos = pygame.mouse.get_pos()
                if self.t1.getStatus():
                    self.c1.setCoord(((pos[0]/32 )*32 - (x%32)),((pos[1]/32 )*32 - (y%32)))
                    self.c1.blit()
                if self.t2.getStatus():
                    self.c2.setCoord(((pos[0]/32 )*32 - (x%32)),((pos[1]/32 )*32 - (y%32)))
                    self.c2.blit()
                ##############    

            
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

            
    def tick(self,ticks,x,y,level):
        self.time = ticks/60
        if gui.gameOver==True or gui.defeat==True:
            if pygame.mouse.get_pressed()[0]==True:
                gui.gameOver=False
                gui.scorePosted = False
                Game.menu1(gui.screen)
        #################
        if level.player == None:
                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]==True:
                    if self.t1.clicked() and self.t1.getStatus() == 0:
                         print 1
                         self.t1.setOne()
                         self.t2.setZero()
                    if self.t2.clicked() and self.t1.getStatus() == 0:
                         print 1
                         self.t2.setOne()
                         self.t1.setZero()

                
                elif self.t1.getStatus() == 1:
                        self.t1.setZero()
                        p = pygame.mouse.get_pos() 
                        if self.t1.collide(p) == 0:
                            gui.level.setTile(pos[0]/32 + x/32,pos[1]/32 + y/32,Tile.Treasure1)

                elif self.t2.getStatus() == 1:
                    self.t2.setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t2.collide(p) == 0:
                            gui.level.setTile(pos[0]/32 + x/32,pos[1]/32 + y/32,Tile.Treasure2)
                
        ##################
                                     
        

        
