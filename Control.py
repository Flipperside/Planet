import pygame
import sys
from asteroid import Asteroid


def events(sun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #ВПраво
            if event.key == pygame.K_d:
                sun.right = True
            #ВЛево
            if event.key == pygame.K_a:
                sun.left = True
            #Вверх
            if event.key == pygame.K_w:
                sun.up = True
            #Вниз
            if event.key == pygame.K_s:
                sun.down = True
        elif event.type == pygame.KEYUP:
            #ВПраво
            if event.key == pygame.K_d:
                sun.right = False
            #ВЛево
            if event.key == pygame.K_a:
                sun.left = False
            #Вверх
            if event.key == pygame.K_w:
                sun.up = False
            #Вниз
            if event.key == pygame.K_s:
                sun.down = False


def spawn(time, screen, asteroids):
    if time % 300 == 0:
        new_aster = Asteroid(screen)
        asteroids.add(new_aster)


def update(bg_color, screen, asteroids, sun, planet):
    screen.fill(bg_color)
    for asteroid in asteroids.sprites():
        asteroid.output()
    planet.output()
    sun.output()
    pygame.display.flip()


def update_asteroid(asteroids, sun):
    asteroids.update()
    hit = pygame.sprite.spritecollide(sun, asteroids, True)
    print(hit)

