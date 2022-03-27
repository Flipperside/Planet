import pygame


class Sun:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('images/Sun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center1 = float(self.rect.centerx)
        self.rect.centery = self.screen_rect.centery
        self.center2 = float(self.rect.centery)
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_sun(self):

        if self.right and self.rect.right < self.screen_rect.right + 150:
            self.center1 += 1
        if self.left and self.rect.left > self.screen_rect.left - 150:
            self.center1 -= 1
        if self.up and self.rect.top > self.screen_rect.top - 150:
            self.center2 -= 1
        if self.down and self.rect.bottom < self.screen_rect.bottom + 150:
            self.center2 += 1
        self.rect.centerx = self.center1
        self.rect.centery = self.center2
        print(self.rect.centerx)


