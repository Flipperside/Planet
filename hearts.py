import pygame


class Hearts:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/Heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1750
        self.rect.y = 20

    def output(self):
        self.screen.blit(self.image, self.rect)