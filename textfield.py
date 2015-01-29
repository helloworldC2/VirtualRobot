# -*- coding: cp1252 -*-
import pygame
import sys
from pygame.locals import *

class textField :
    def __init__(self,canvas,x,y,hossz,magassag,s,betumeret):
        self.disp = canvas 
        self.posX = x
        self.posY = y
        self.w = hossz
        self.h = magassag
        self.fontH = betumeret
        self.answer = str()
        self.selected = False
        #initializing font
        pygame.font.init()
        #setting up font type 
        font = pygame.font.SysFont("monospace",15)
        #fake rendering bold text
        font.set_bold(1)
        text = font.render(s,1,(0,0,0))
        return

    def blit(self):
        tmp = self.answer
        if self.isSelected():
            tmp += '_'
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        #printing the rects
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        self.disp.blit(text,(self.posX,self.posY))
        #update screen
        pygame.display.update()
        return


    #reprinting the textfield when the user writes or deletes something
    def reprint(self,string): 
        tmp = string
        if self.isSelected():
            tmp += '_'
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        
        self.disp.blit(text,(self.posX,self.posY))
        
        pygame.display.update()
        
        
        return

    def handle(self,event):
            #string for the answer 
            #answer = str()
            #self.answer += '_'
             
                            #if user presses a key
                                #if backspace, delete the last char from string
            if event.key == K_BACKSPACE:
                                    self.answer = self.answer[:-1]
                                    #self.answer = self.answer[:-1]
                                    #self.answer += '_'
                                    print self.answer
            elif event.key == K_RETURN:
                                    #self.answer = self.answer[:-1]
                                    self.reprint(self.answer)
                                    return self.answer
                                    
                                #add the new characters to the string
            elif event.key == pygame.K_QUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + \'"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '@'
                                    #self.answer += '_'
            elif event.key == pygame.K_SEMICOLON and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + ;"
                                    #self.answer = self.answer[:-1]
                                    self.answer += ':'
                                    #self.answer += '_'
            elif event.key == pygame.K_HASH and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + #"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '~'
                                    #self.answer += '_'
            elif event.key == pygame.K_LEFTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + ["
                                    #self.answer = self.answer[:-1]
                                    self.answer += '{'
            elif event.key == pygame.K_RIGHTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + ]"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '}'
                                    #self.answer += '_'
            elif event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + ="
                                    #self.answer = self.answer[:-1]
                                    self.answer += '+'
                                    #self.answer += '_'
            elif event.key == pygame.K_MINUS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + -"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '_'
                                    #self.answer += '_'
            elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 0"
                                    #self.answer = self.answer[:-1]
                                    self.answer += ')'
                                    #self.answer += '_'
            elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 9"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '('
                                    #self.answer += '_'
            elif event.key == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 8"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '*'
                                    #self.answer += '_'
            elif event.key == pygame.K_7 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 7"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '&'
                                    #self.answer += '_'
            elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 6"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '^'
                                    #self.answer += '_'
            elif event.key == pygame.K_5 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 5"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '%'
                                    #self.answer += '_'
            elif event.key == pygame.K_4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 4"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '$'
                                    #self.answer += '_'
            elif event.key == pygame.K_3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 3"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '£'
                                    #self.answer += '_'
            elif event.key == pygame.K_2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 2"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '\"'
                                    #self.answer += '_'
            elif event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + 1"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '!'
                                    #self.answer += '_'
            elif event.key == pygame.K_BACKQUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                    print "pressed: SHIFT + `"
                                    #self.answer = self.answer[:-1]
                                    self.answer += '¬'
                                    #self.answer += '_'

                                    
            elif event.key <= 127:
                                    #self.answer = self.answer[:-1]
                                    self.answer += (chr(event.key))
                                    #self.answer += '_'
                            #reprinting everything with the new string   
            self.reprint(self.answer)
            return

    def collide(self, pos) :
        if (pos[0] >= self.posX and pos[0] <=self.posX + self.w and
            pos[1] >= self.posY and pos[1] <= self.posY + self.h) :
            return 1
        else :
            return 0
        return

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.collide(pos):
            return 1
        else:
            return 0
        return

    def isSelected(self):
        if self.selected == False:
            return 0
        else:
            return 1
        return

    def select(self):
        self.selected = True
        self.reprint(self.answer)
        return

    def off(self):
        self.selected = False
        self.reprint(self.answer)
        return
        



