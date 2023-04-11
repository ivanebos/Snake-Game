import random
import pygame


class Food:
    def __init__(self,win_size,size):

        self.size = size

        self.win_size = win_size
        self.posy = random.randint(1,self.size-1)
        self.posx = random.randint(1,self.size-1)
        self.gap = (self.win_size-1)/self.size
    
    def draw(self):

        self.rect = pygame.Rect(self.posy*self.gap+1, self.posx*self.gap+1, self.gap,self.gap)
        return self.rect


    def genNewFood(self):
        self.posy = random.randint(1,self.size-1)
        self.posx = random.randint(1,self.size-1)

        



