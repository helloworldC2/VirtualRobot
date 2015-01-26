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
        #initializing font
        pygame.font.init()
        #setting up font type 
        font = pygame.font.SysFont("monospace",15)
        #fake rendering bold text
        font.set_bold(1)
        text = font.render(s,1,(0,0,0))
        self.disp.blit(text,(self.posX-len(s)*12,self.posY))
        #the rectangle for the actual textfield 
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        #printing the rects
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        #update screen
        pygame.display.update()
        return

    #reprinting the textfield when the user writes or deletes something
    def reprint(self,string): 
        
        font = pygame.font.SysFont("monospace",self.fontH)
        text = font.render(string,1,(0,0,0))
        
        r1 = pygame.Rect(self.posX,self.posY,self.w,self.h)
        r2 = pygame.Rect(self.posX-2,self.posY-2,self.w+4,self.h+4)
        pygame.draw.rect(self.disp, (0,0,0),r2)
        pygame.draw.rect(self.disp, (255,255,255),r1)
        
        self.disp.blit(text,(self.posX,self.posY))
        
        pygame.display.update()
        
        
        return

    def ask(self):
        #string for the answer 
        answer = str()
        answer += '_'
        while True:
                for event in pygame.event.get():
                    #if user hits x button
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        #if user presses a key
                        if event.type == KEYDOWN:
                            #if backspace, delete the last char from string
                            if event.key == K_BACKSPACE:
                                answer = answer[:-1]
                                answer = answer[:-1]
                                answer += '_'
                                print answer
                            elif event.key == K_RETURN:
                                answer = answer[:-1]
                                self.reprint(answer)
                                return answer
                                break
                            #add the new characters to the string
                            elif event.key == pygame.K_QUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + \'"
                                answer = answer[:-1]
                                answer += '@'
                                answer += '_'
                            elif event.key == pygame.K_SEMICOLON and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + ;"
                                answer = answer[:-1]
                                answer += ':'
                                answer += '_'
                            elif event.key == pygame.K_HASH and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + #"
                                answer = answer[:-1]
                                answer += '~'
                                answer += '_'
                            elif event.key == pygame.K_LEFTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + ["
                                answer = answer[:-1]
                                answer += '{'
                            elif event.key == pygame.K_RIGHTBRACKET and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + ]"
                                answer = answer[:-1]
                                answer += '}'
                                answer += '_'
                            elif event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + ="
                                answer = answer[:-1]
                                answer += '+'
                                answer += '_'
                            elif event.key == pygame.K_MINUS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + -"
                                answer = answer[:-1]
                                answer += '_'
                                answer += '_'
                            elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 0"
                                answer = answer[:-1]
                                answer += ')'
                                answer += '_'
                            elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 9"
                                answer = answer[:-1]
                                answer += '('
                                answer += '_'
                            elif event.key == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 8"
                                answer = answer[:-1]
                                answer += '*'
                                answer += '_'
                            elif event.key == pygame.K_7 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 7"
                                answer = answer[:-1]
                                answer += '&'
                                answer += '_'
                            elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 6"
                                answer = answer[:-1]
                                answer += '^'
                                answer += '_'
                            elif event.key == pygame.K_5 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 5"
                                answer = answer[:-1]
                                answer += '%'
                                answer += '_'
                            elif event.key == pygame.K_4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 4"
                                answer = answer[:-1]
                                answer += '$'
                                answer += '_'
                            elif event.key == pygame.K_3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 3"
                                answer = answer[:-1]
                                answer += '£'
                                answer += '_'
                            elif event.key == pygame.K_2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 2"
                                answer = answer[:-1]
                                answer += '\"'
                                answer += '_'
                            elif event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + 1"
                                answer = answer[:-1]
                                answer += '!'
                                answer += '_'
                            elif event.key == pygame.K_BACKQUOTE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                print "pressed: SHIFT + `"
                                answer = answer[:-1]
                                answer += '¬'
                                answer += '_'

                                
                            elif event.key <= 127:
                                answer = answer[:-1]
                                answer += (chr(event.key))
                                answer += '_'
                        #reprinting everything with the new string   
                        self.reprint(answer)
        return


