import pygame
import Control
from planet import Planet
from sun import Sun
from Asteroid import Asteroid


W, H = 1920, 1080


def run():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Space battle')
    bg_color = (0, 0, 0)
    planet = Planet(screen)
    sun = Sun(screen)

    while True:
        Control.events(sun)
        sun.update_sun()
        Control.update(bg_color, screen, sun, planet)




run()

