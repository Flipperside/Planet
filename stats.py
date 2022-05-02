import pygame


class Stats:

    def __init__(self):
        self.life = 3
        self.score = 0
        with open('score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def output(self):
        self.screen.blit(self.image, self.rect)
