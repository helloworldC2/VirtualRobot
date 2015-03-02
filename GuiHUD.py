import scoring
import pygame
import gui
import Game
import selectBar
from selectBar import *
import Level
from Level import *
import Tile
import EntityTreasure



class GuiHUD(object):


    def __init__(self,screen):
        self.time = 1
        self.healthbar = pygame.image.load('menu/Healthbar.png')
        self.bar = image(screen,(20,494),"menu/bar.png")
        self.t = [image(screen,(30,500),"tiles/brokenChest.png"),
             image(screen,(90,500),"tiles/burntChest.png"),
             image(screen,(150,500),"tiles/darkChest.png"),
             image(screen,(210,500),"tiles/glassChest.png"),
             image(screen,(270,500),"tiles/goldChest.png"),
             image(screen,(330,500),"tiles/normalChest.png"),
             image(screen,(390,500),"tiles/OverFlowChest.png"),
             image(screen,(450,500),"tiles/crystalChest.png"),
             image(screen,(510,500),"tiles/sandT.png"),
             image(screen,(570,500),"tiles/grownOverChest.png")]
            
        for i in range (10):
                  self.t[i].scale(48,48)

        self.c = [image(screen,(30,500),"tiles/brokenChest.png"),
             image(screen,(80,500),"tiles/burntChest.png"),
             image(screen,(130,500),"tiles/darkChest.png"),
             image(screen,(180,500),"tiles/glassChest.png"),
             image(screen,(230,500),"tiles/goldChest.png"),
             image(screen,(280,500),"tiles/normalChest.png"),
             image(screen,(330,500),"tiles/OverFlowChest.png"),
             image(screen,(380,500),"tiles/crystalChest.png"),
             image(screen,(430,500),"tiles/sandT.png"),
             image(screen,(480,500),"tiles/grownOverChest.png")]

        for i in range (10):
                  self.c[i].scale(32,32)
        return
    
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
                pygame.draw.circle(screen, (255,0,0), (0,600), int(120*(level.player.health/100.00)))
                pygame.draw.circle(screen, (0,0,255), (800,600), int(120*(level.player.health/100.00)))
                screen.blit(self.healthbar, (-140,450))
                screen.blit(self.healthbar, (650,450))
                #pygame.draw.rect(screen,(255,0,0),(10,170,110,10))
                #pygame.draw.rect(screen,(0,255,0),(10,170,level.player.health,10))
                text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
                textpos = text.get_rect(center=(60,60))
                screen.blit(text, textpos)

            if level.player == None:
                ##############
                self.bar.blit()
                for i in range(10):
                    self.t[i].blit()
                    
                pos = pygame.mouse.get_pos()
                pX = ((pos[0]/32 )*32 - (x%32))
                pY = ((pos[1]/32 )*32 - (y%32))

                for i in range(10):
                    if self.t[i].getStatus():
                        self.c[i].setCoord(pX,pY)
                        self.c[i].blit()

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
                #text2 = font.render("Health bar:", True, (0,0,0))
                #textpos2 = text.get_rect(center=(60,150))
                #screen.blit(text2, textpos2)

            
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
                    for i in range(10):
                        if self.t[i].clicked() and self.t[i].getStatus() == 0:
                            
                            self.t[i].setOne()
                            for j in range(10):
                                if j != i:
                                    self.t[j].setZero()
                
                elif self.t[0].getStatus() == 1:
                        self.t[0].setZero()
                        p = pygame.mouse.get_pos() 
                        if self.t[0].collide(p) == 0:
                            try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/brokenChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[1].getStatus() == 1:
                    self.t[1].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[1].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/burntChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"
                                gui.level.player = gui.player
                                
                elif self.t[2].getStatus() == 1:
                    self.t[2].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[2].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/darkChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[3].getStatus() == 1:
                    self.t[3].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[3].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/glassChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[4].getStatus() == 1:
                    self.t[4].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[4].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/goldChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"
                elif self.t[5].getStatus() == 1:
                    self.t[5].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[5].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/normalChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[6].getStatus() == 1:
                    self.t[6].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[6].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/OverFlowChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"


                elif self.t[7].getStatus() == 1:
                    self.t[7].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[7].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/crystalChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[8].getStatus() == 1:
                    self.t[8].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[8].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/sandT.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"

                elif self.t[9].getStatus() == 1:
                    self.t[9].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[9].collide(p) == 0:
                        try:
                                gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                        except:
                                gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/grownOverChest.png")))
                                gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                print "placed"



                
        ##################
                                     
        

        
