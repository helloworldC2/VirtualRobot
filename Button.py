import Image
import pygame

class button(Image.image):    
    def collide(self,pos) :
        rect = self.img.get_rect()
        if pos[0] >= self.x and pos[0] <=self.x + rect.width and pos[1] >= self.y and pos[1] <= self.y + rect.height :
            return 1
        else :
            return 0

    def clicked(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if self.collide(pos) == 1 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return 1
            else:
                return 0


