import pygame


class Planet(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Planet, self).__init__()

        self.screen = screen
        self.image = pygame.image.load('images/planet.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def output(self):
        self.screen.blit(self.image, self.rect)
