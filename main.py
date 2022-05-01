import pygame
import Control
from planet import Planet
from sun import Sun
from pygame.sprite import Group
from stats import Stats
from currectLife import Life
from hearts import Hearts
from button import Button
import sys


FPS = 300
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
bg_menu = pygame.image.load('images/Menu.jpg')


def show_menu():
    pygame.init()
    start = Button(300, 70, screen)
    rule = Button(300, 70, screen)
    quit_b = Button(300, 70, screen)
    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(bg_menu, (0, 0))
        start.draw(790, 340, 'Новая игра', run)
        rule.draw(790, 440, 'Правила')
        quit_b.draw(790, 540, 'Выйти', quit)

        pygame.display.update()
        clock.tick(FPS)


def run():
    global screen
    pygame.init()
    pygame.display.set_caption('Space battle')
    bg_color = (0, 0, 0)
    hearts = Hearts(screen)
    planet = Planet(screen)
    sun = Sun(screen)
    asteroids = Group()
    stats = Stats()
    hp = Life(screen, stats)
    button = Button(100, 50, screen)
    time = 0

    while True:
        time += 1
        Control.spawn(time, screen, asteroids)
        Control.events(sun)
        sun.update_sun()
        Control.update_asteroid(asteroids, sun, planet, stats, hp)
        Control.update(bg_color, screen, asteroids, sun, planet, stats, hp, hearts, button)
        clock.tick(FPS)
        print(stats.life)


show_menu()
