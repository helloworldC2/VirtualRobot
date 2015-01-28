#Sounds
import pygame
import Game
import random


sound_list = ['menu/asda.wav','menu/asda2.wav','menu/Track1ad.wav']
def playMusic():
    return sound_list[random.randint(0,len(sound_list)-1)]

def Plysound(hoverOn,hit,bClick,trFound):
    soundNumb = 0
    hov = ['sound/hover.wav','sound/Hitsound.wav','sound/treasureFound.wav','sound/Click.wav']
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
        
