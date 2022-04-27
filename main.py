import pygame
import Control
from planet import Planet
from sun import Sun
from pygame.sprite import Group
FPS = 100


def run():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Space battle')
    bg_color = (0, 0, 0)
    planet = Planet(screen)
    sun = Sun(screen)
    asteroids = Group()
    time = 0
    while True:
        time += 1
        Control.spawn(time, screen, asteroids)
        Control.events(sun)
        sun.update_sun()
        Control.update_asteroid(asteroids)
        Control.update(bg_color, screen, asteroids, sun, planet)
        clock.tick(FPS)







run()

