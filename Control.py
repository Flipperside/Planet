import pygame
import sys


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


def update(bg_color, screen, asteroid, sun, planet):
    screen.fill(bg_color)
    planet.output()
    sun.output()
    asteroid.output()
    pygame.display.flip()

