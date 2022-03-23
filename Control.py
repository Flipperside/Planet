import pygame
import sys


def events(sun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Право
            if event.key == pygame.K_d:
                sun.right = True
            #Лево
            if event.key == pygame.K_a:
                sun.left = True
            #Вверх
            if event.key == pygame.K_w:
                sun.up = True
            if event.key == pygame.K_s:
                sun.down = True
        elif event.type == pygame.KEYUP:
            #Право
            if event.key == pygame.K_d:
                sun.right = False
            #Лево
            if event.key == pygame.K_a:
                sun.left = False
            # Вверх
            if event.key == pygame.K_w:
                sun.up = False
            if event.key == pygame.K_s:
                sun.down = False


def update(bg_color, screen, sun, planet):
    screen.fill(bg_color)
    planet.output()
    sun.output()
    pygame.display.flip()