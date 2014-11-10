#Sounds
import pygame

sounds = []

class Sound(object):
    def __init__(self,id,path):
        pygame.mixer.init(44100, -16,2,2048)
        sound = pygame.mixer.music.load(path)
        sounds.append(self)
    def play(self):
        sound.play()


example = Sound(0,"exapmle.wav")
example2 = Sound(1,"exapmle1.wav")



#to play

#Sound.sounds[id].play()
