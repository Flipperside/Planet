import pygame


def print_text(massage, x, y, screen, font_color=(0, 0, 0), font_type='arial.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(massage, True, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.button_sound = pygame.mixer.Sound('button.wav')
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, massage, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
            print_text(massage, x, y, self.screen)

            if click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(self.button_sound)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))

            print_text(massage, x, y, self.screen)

