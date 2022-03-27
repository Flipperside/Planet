import pygame
import Control
from planet import Planet
from sun import Sun
from asteroid import Asteroid


def run():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('Space battle')
    bg_color = (0, 0, 0)
    planet = Planet(screen)
    sun = Sun(screen)
    asteroid = Asteroid(screen)

    while True:
        Control.events(sun)
        sun.update_sun()
        asteroid.update_aster()
        Control.update(bg_color, screen, asteroid, sun, planet)





run()

