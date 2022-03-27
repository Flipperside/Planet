import pygame
import random


class Asteroid:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('images/Aster.png')
        self.rect = self.image.get_rect()
        self.pos = random.randint(1, 2)
        if self.pos == 1:
            self.rect.x = random.randrange(0, 1920, 1919)
            self.rect.y = random.randrange(0, 1080)
        else:
            self.rect.x = random.randint(0, 1920)
            self.rect.y = random.randrange(0, 1080, 1079)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_aster(self):
        vektorx = 900 - self.x
        vektory = 500 - self.y
        self.x += vektorx / 1000
        self.y += vektory / 1000
        self.rect.x = self.x
        self.rect.y = self.y

