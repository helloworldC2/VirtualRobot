"""By Hello World  ©2014
  George Claridge
  Aaron Daisley
  Ricky Singh
  Joel Bradley
  Adam Cook
  Ben Domokos
"""
import pygame

#so it begins
print "Hello, world!"

class Game():


    def run(self):
      while True:
          pygame.display.update()
          self.fpsClock.tick(60)
          
    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width,height))
        self.fpsClock = pygame.time.Clock()
        #font = pygame.font.Font('freesansbold.ttf', 36)
        self.run()
        
    
          

if __name__ == "__main__":
    width = 600
    height = 400
    game = Game(width, height)

pygame.quit()

