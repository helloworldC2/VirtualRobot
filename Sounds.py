#Sounds
import pygame
import Game
import random
import os


class Audio():
    def __init__(self,mute):
        self.mute = mute   
        
    def playMusic(self):
        self.music =['menu/asda.wav']
        pygame.mixer.music.load('menu/asda.wav')
        pygame.mixer.music.play(0)
  
    def Plysound(self,hoverOn,hit,bClick,trFound,Dquack):
        soundNumb = 0
        hov = ['sound/hover.wav','sound/Hitsound.wav','sound/treasureFound.wav','sound/Click.wav','sound/Duck.wav']
        if hit == True:
            soundNumb = 1
            soundz = pygame.mixer.Sound(hov[soundNumb])
            pygame.mixer.Sound.play(soundz)
        if hoverOn == True:
            soundNumb = 0
            soundz = pygame.mixer.Sound(hov[soundNumb])
            pygame.mixer.Sound.play(soundz)
        if hoverOn == True:
            leng = 400
            pygame.mixer.Sound.fadeout(soundz,leng)
        if trFound == True:
            pass
        if bClick == True:
            soundNumb = 3
            soundz = pygame.mixer.Sound(hov[soundNumb])
            pygame.mixer.Sound.play(soundz)
        if trFound == True:
            soundNumb = 2
            soundz = pygame.mixer.Sound(hov[soundNumb])
            pygame.mixer.Sound.play(soundz)
        if Dquack == True:
            soundNumb = 4
            soundz = pygame.mixer.Sound(hov[soundNumb])
            pygame.mixer.Sound.play(soundz)
        
