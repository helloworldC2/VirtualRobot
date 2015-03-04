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
import Keyboard



class GuiHUD(object):


    def __init__(self,screen):
        self.tmp = 0 
        self.time = 1
        self.box = barItem(screen,(0,0),"tiles/select.png")
        self.trap = [barItem(screen,(30,500),"tiles/cactus.png"),
                     barItem(screen,(90,500),"tiles/ditch1.png"),
                     barItem(screen,(150,500),"tiles/larval.png"),
                     barItem(screen,(210,500),"tiles/btgrass.png")]

        for i in self.trap:
            i.scale(48,48)
                     
        
        self.healthbar = pygame.image.load('menu/Healthbar.png')
        self.bar = barItem(screen,(20,494),"menu/bar.png")
        self.t = [barItem(screen,(30,500),"tiles/brokenChest.png"),
             barItem(screen,(90,500),"tiles/burntChest.png"),
             barItem(screen,(150,500),"tiles/darkChest.png"),
             barItem(screen,(210,500),"tiles/glassChest.png"),
             barItem(screen,(270,500),"tiles/goldChest.png"),
             barItem(screen,(330,500),"tiles/normalChest.png"),
             barItem(screen,(390,500),"tiles/OverFlowChest.png"),
             barItem(screen,(450,500),"tiles/crystalChest.png"),
             barItem(screen,(510,500),"tiles/sandT.png"),
             barItem(screen,(570,500),"tiles/grownOverChest.png")]
            
        for i in range (10):
                  self.t[i].scale(48,48)

        self.c = [barItem(screen,(30,500),"tiles/brokenChest.png"),
             barItem(screen,(80,500),"tiles/burntChest.png"),
             barItem(screen,(130,500),"tiles/darkChest.png"),
             barItem(screen,(180,500),"tiles/glassChest.png"),
             barItem(screen,(230,500),"tiles/goldChest.png"),
             barItem(screen,(280,500),"tiles/normalChest.png"),
             barItem(screen,(330,500),"tiles/OverFlowChest.png"),
             barItem(screen,(380,500),"tiles/crystalChest.png"),
             barItem(screen,(430,500),"tiles/sandT.png"),
             barItem(screen,(480,500),"tiles/grownOverChest.png")]

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
                gui.gameOver = False
                gui.defeat = False 
                 
                        
        else:
            if level.player!=None:
                i = 3
                
                    
                
                pygame.draw.circle(screen, (255,0,0), (0,600), int(120*(level.player.health/100.00)))
                pygame.draw.circle(screen, (0,0,255), (800,600), int(120*(level.player.health/100.00)))
                screen.blit(self.healthbar, (-140,450))
                screen.blit(self.healthbar, (650,450))
                #pygame.draw.rect(screen,(255,0,0),(10,170,110,10))
                #pygame.draw.rect(screen,(0,255,0),(10,170,level.player.health,10))
                text = font.render("Score: "+str(level.player.score.score), True, (0,0,0))
                textpos = text.get_rect(center=(60,60))
                screen.blit(text, textpos)
                self.box.scale(52,52)
                self.box.setCoord(self.trap[self.tmp].x-2,self.trap[self.tmp].y-2)
               
                self.bar.blit()
                
                for tr in self.trap:
                    tr.blit()
                self.box.blit()
                

            if level.player == None:
                ##############
                self.bar.blit()
                for i in range(10):
                    if self.t[i].ifPlaced() == False:
                        self.t[i].blit()
                    
                pos = pygame.mouse.get_pos()
                pX = ((pos[0]/32 )*32 - (x%32))
                pY = ((pos[1]/32 )*32 - (y%32))

                for i in range(10):
                    if self.t[i].ifPlaced() == False:
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
        
        if Keyboard.keys['right']==True:
            Keyboard.keys['right']=False
            self.tmp +=1
            self.tmp = self.tmp%4

        if Keyboard.keys['left']==True:
            Keyboard.keys['left']=False
            self.tmp -=1
            self.tmp = self.tmp%4

        #print self.tmp

        self.time = ticks/60

        #if level.player != None:
            
            
        
        if gui.gameOver==True or gui.defeat==True:
            Game.menu1(gui.screen)
            if pygame.mouse.get_pressed()[0]==True:
                gui.gameOver=False
                gui.scorePosted = False
             
        #################
        elif level.player == None:
                pos = pygame.mouse.get_pos()
                r = 1
                for i in range(10):
                    if self.t[i].getStatus():
                        r = 0
                if pygame.mouse.get_pressed()[0]==True :
                    for i in range(10):
                        if self.t[i].clicked() and self.t[i].getStatus() == 0 and r:
                            
                            self.t[i].setOne()
                            for j in range(10):
                                if j != i:
                                    self.t[j].setZero()
                
                elif self.t[0].getStatus() == 1 :
                        self.t[0].setZero()
                        p = pygame.mouse.get_pos() 
                        if self.t[0].collide(p) == 0:
                            if self.t[0].ifPlaced() == False:
                                try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/brokenChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[0].place()

                elif self.t[1].getStatus() == 1:
                    self.t[1].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[1].collide(p) == 0:
                        if self.t[1].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/burntChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[1].place()
                                    gui.level.player = gui.player
                                
                elif self.t[2].getStatus() == 1:
                    self.t[2].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[2].collide(p) == 0:
                        if self.t[2].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/darkChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[2].place()

                elif self.t[3].getStatus() == 1:
                    self.t[3].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[3].collide(p) == 0:
                        if self.t[3].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/glassChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[3].place()

                elif self.t[4].getStatus() == 1:
                    self.t[4].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[4].collide(p) == 0:
                        if self.t[4].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/goldChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[4].place()
                                
                elif self.t[5].getStatus() == 1:
                    self.t[5].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[5].collide(p) == 0:
                        if self.t[5].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/normalChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[5].place()

                elif self.t[6].getStatus() == 1:
                    self.t[6].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[6].collide(p) == 0:
                        if self.t[6].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/OverFlowChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[6].place()


                elif self.t[7].getStatus() == 1:
                    self.t[7].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[7].collide(p) == 0:
                        if self.t[7].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/crystalChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[7].place()

                elif self.t[8].getStatus() == 1:
                    self.t[8].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[8].collide(p) == 0:
                        if self.t[8].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/sandT.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[8].place()

                elif self.t[9].getStatus() == 1:
                    self.t[9].setZero()
                    p = pygame.mouse.get_pos() 
                    if self.t[9].collide(p) == 0:
                        if self.t[9].ifPlaced() == False:
                            try:
                                    gui.treasureLocations.index((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                            except:
                                    gui.level.entities.append(EntityTreasure.EntityTreasure(gui.level,((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5,10,pygame.image.load("tiles/grownOverChest.png")))
                                    gui.treasureLocations.append((((pos[0]>>5)+(x>>5))<<5,((pos[1]>>5)+(y>>5))<<5))
                                    print "placed"
                                    self.t[9].place()



                
        ##################
                                     
        

        
