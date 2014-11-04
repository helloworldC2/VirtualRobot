#Sounds
import pygame

sounds = []

class Sound(self):
    def __init__(self,id,path):
        sound = pygame.mixer.music.load(path)
        sounds.append(self)
    def play(self):
        sound.play()


example = Sound(0,"exapmle.wav")
example2 = Sound(1,"exapmle1.wav")



#to play

#Sound.sounds[id].play()
