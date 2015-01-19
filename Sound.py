#Sounds
import pygame
import Game
import random


sound_list = ['menu/asda.wav','menu/asda2.wav','menu/Track1ad.wav']
def random_sound():
    return sound_list[random.randint(0,len(sound_list)-1)]
