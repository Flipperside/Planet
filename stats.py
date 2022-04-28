import pygame


class Stats:

    def __init__(self):
        self.life = 3

    def output(self):
        self.screen.blit(self.image, self.rect)

