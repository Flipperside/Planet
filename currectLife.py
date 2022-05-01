import pygame.font


class Life:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (200, 0, 0)
        self.font = pygame.font.SysFont(None, 100)
        self.image_life()

    def image_life(self):

        self.life_img = self.font.render(str(self.stats.life), True, self.text_color, (0, 0, 0))
        self.life_rect = self.life_img.get_rect()
        self.life_rect.right = self.screen_rect.right - 40
        self.life_rect.top = 20

    def show_life(self):

        self.screen.blit(self.life_img, self.life_rect)

