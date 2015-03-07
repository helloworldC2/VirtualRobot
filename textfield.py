# -*- coding: cp1252 -*-
import pygame
import sys
from pygame.locals import *

class textField :
    def __init__(self,canvas,(x,y),(hossz,magassag),s,betumeret):
        self.disp = canvas 
        self.posX = x
        self.posY = y
        self.fontY = y
        self.w = hossz
        self.h = magassag
        self.fontH = betumeret
        self.answer = s
        self.num = 0
        self.selected = False
        
        #initializing font
        pygame.font.init()
        
        #setting up font type 
        font = pygame.font.SysFont("monospace",15)
        
        #fake rendering bold text
        font.set_bold(1)
        text = font.render(s,1,(0,0,0))
        return


    #gets: self
    #returns: nothing
    def blit(self):
        tmp = self.answer
        if self.isSelected():
            tmp += '_'
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        rect = text.get_rect()
        #print rect
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        #printing the rects
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        self.disp.blit(text,(self.posX,self.fontY+2))
        #update screen
        #pygame.display.update()
        return


    #reprinting the textfield when the user writes or deletes something
    def reprint(self,string): 
        tmp = string
        if self.isSelected():
            tmp += '_'
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        rect = text.get_rect()
        #print rect
        if rect.width >= self.w - 8 and self.fontH > 11:
            self.fontH -= 1
            self.fontY += 1
            self.reprint(string)
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        
        self.disp.blit(text,(self.posX,self.fontY+2))
        
        pygame.display.update()
        return

    def numHandle(self,event):
        tmp = self.answer
        if self.isSelected():
            tmp += '_'
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        rect = text.get_rect()
        #print rect
        
        if event == K_BACKSPACE:
            self.answer = self.answer[:-1]
            print self.answer
            self.blit()

        elif rect.width <= self.w-5:
                if event == pygame.K_0 :
                                        print "pressed: 0"
                                        self.answer += '0'
                elif event == pygame.K_9 :
                                        print "pressed: 9"
                                        self.answer += '9'
                elif event == pygame.K_8 :
                                        print "pressed: 8"
                                        self.answer += '8'
                elif event == pygame.K_7 :
                                        print "pressed: 7"
                                        self.answer += '7'
                elif event == pygame.K_6 :
                                        print "pressed: 6"
                                        self.answer += '6'
                elif event == pygame.K_5 :
                                        print "pressed: 5"
                                        self.answer += '5'
                elif event == pygame.K_4 :
                                        print "pressed: 4"
                                        self.answer += '4'
                elif event == pygame.K_3 :
                                        print "pressed: 3"
                                        self.answer += '3'
                elif event == pygame.K_2 :
                                        print "pressed: 2"
                                        self.answer += '2'
                elif event == pygame.K_1 :
                                        print "pressed: 1"
                                        self.answer += '1'
        self.reprint(self.answer)
        return


    
    #This class is handling the user's input in the textfield
    #gets: key
    #returns: nothing
    def handle(self,event):
        tmp = self.answer
        if self.isSelected():
            tmp += '_'
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(tmp,1,(0,0,0))
        rect = text.get_rect()
        #print rect
        if event == K_BACKSPACE:
            self.answer = self.answer[:-1]
            print self.answer
            self.blit()
            
        elif rect.width <= self.w-5:
            
            #if user presses a key
            #if backspace, delete the last char from string
                
                if event == K_RETURN:
                                        
                                        self.reprint(self.answer)
                                        return self.answer
                                        
                #add the new characters to the string
                elif event == pygame.K_QUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + \'"
                                        self.answer += '@'
                elif event == pygame.K_SEMICOLON and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + ;"
                                        self.answer += ':'
                elif event == pygame.K_HASH and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + #"
                                        self.answer += '~'
                elif event == pygame.K_LEFTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + ["
                                        self.answer += '{'
                elif event == pygame.K_RIGHTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + ]"
                                        self.answer += '}'
                elif event == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + ="
                                        self.answer += '+'
                elif event == pygame.K_MINUS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + -"
                                        self.answer += '_'
                elif event == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 0"
                                        self.answer += ')'
                elif event == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 9"
                                        self.answer += '('
                elif event == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 8"
                                        self.answer += '*'
                elif event == pygame.K_7 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 7"
                                        self.answer += '&'
                elif event == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 6"
                                        self.answer += '^'
                elif event == pygame.K_5 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 5"
                                        self.answer += '%'
                elif event == pygame.K_4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 4"
                                        self.answer += '$'
                elif event == pygame.K_3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 3"
                                        self.answer += '£'
                elif event == pygame.K_2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 2"
                                        self.answer += '\"'
                elif event == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + 1"
                                        self.answer += '!'
                elif event == pygame.K_BACKQUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                        print "pressed: SHIFT + `"
                                        self.answer += '¬'
                elif pygame.key.get_mods() & pygame.KMOD_SHIFT :
                    if event >= 97 and event <= 122:
                        print "pressed: SHIFT +",chr(event)
                        self.answer += (chr(event-32))
                                        
                elif event <= 127 and event >= 32:
                                        self.answer += (chr(event))
                                        
                #reprinting everything with the new string   
                self.reprint(self.answer)
        return

    #This function detects if the button is over the textfield
    #gets: self, mouse position
    #returns: True if mouse is over, False if not
    def collide(self, pos) :
        if (pos[0] >= self.posX and pos[0] <=self.posX + self.w and
            pos[1] >= self.posY and pos[1] <= self.posY + self.h) :
            return 1
        else :
            return 0
        return

    #This function detects if the textfield was clicked
    #gets: self
    #returns True if clicked, False if not
    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.collide(pos):
            return 1
        else:
            return 0
        return

    #Tells if the textfield is selected
    #gets: self
    #returns: True if selected, False if not
    def isSelected(self):
        if self.selected == False:
            return 0
        else:
            return 1
        return

    #sets self.selected to True
    def select(self):
        self.selected = True
        self.reprint(self.answer)
        return

    #sets self.selected to False
    def off(self):
        self.selected = False
        self.reprint(self.answer)
        return
        



