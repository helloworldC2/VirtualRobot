#Sounds
import pygame
import Game
import random


sound_list = ['asda.wav','asda2.wav','Track1ad.wav']
def random_sound():
    return sound_list[random.randint(0,len(sound_list)-1)]
