import pygame
import sys
from asteroid import Asteroid
from button import print_text


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


def update(bg_menu, screen, asteroids, sun, planet, stats, hp, hearts):
    screen.blit(bg_menu, (0, 0))
    print_text('Очки', 20, 10, screen, (255, 255, 255))
    print_text(str(stats.score), 165, 10, screen, (255, 255, 255))
    print_text('Рекорд', 380, 10, screen, (255, 255, 255))
    print_text(str(stats.high_score), 600, 10, screen, (255, 255, 255))
    with open('score.txt', 'w') as f:
        f.write(str(stats.high_score))
    hp.show_life()
    if stats.score > stats.high_score:
        stats.high_score = stats.score
    for asteroid in asteroids.sprites():
        asteroid.output()
    planet.output()
    sun.output()
    hearts.output()
    pygame.display.flip()


def update_asteroid(asteroids, sun, planet, stats, hp):
    asteroids.update()
    if pygame.sprite.spritecollide(sun, asteroids, True):
        stats.score += 10
    if pygame.sprite.spritecollide(planet, asteroids, True):
        stats.life -= 1
        hp.image_life()



