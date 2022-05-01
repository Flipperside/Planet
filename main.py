import pygame
import Control
from planet import Planet
from sun import Sun
from pygame.sprite import Group
from stats import Stats
from currectLife import Life
from hearts import Hearts
from button import Button
from button import print_text


FPS = 300
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
bg_menu = pygame.image.load('images/Background.jpg')
pygame.display.set_caption('Space battle')
destroy = pygame.image.load('images/Destroy.png')


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
        rule.draw(790, 440, 'Правила', rules)
        quit_b.draw(790, 540, 'Выйти', quit)

        pygame.display.update()
        clock.tick(FPS)


def rules():
    pygame.init()
    rule_show = True
    menu_b = Button(170, 70, screen)
    while rule_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg_menu, (0, 0))
        print_text('Играя за Солнце вы должны', 590, 340, screen, (255, 255, 255))
        print_text('сбивать астеройды летящие в землю.', 490, 440, screen, (255, 255, 255))
        print_text('У вас есть 3 жизни, если они закончатся - вы проиграете.', 190, 540, screen, (255, 255, 255))
        print_text('Удачи!', 890, 640, screen, (255, 255, 255))
        menu_b.draw(890, 740, 'Назад', show_menu)
        pygame.display.update()
        clock.tick(FPS)


def loose():
    pygame.init()
    loose_game = True
    menu_b = Button(159, 70, screen)
    again_b = Button(197, 70, screen)
    while loose_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg_menu, (0, 0))
        screen.blit(destroy, (760, 320))
        print_text('Вы проиграли!', 790, 270, screen, (255, 255, 255))
        menu_b.draw(590, 540, 'Меню', show_menu)
        again_b.draw(1200, 540, 'Заново', run)
        pygame.display.update()
        clock.tick(FPS)


def run():
    pygame.init()
    hearts = Hearts(screen)
    planet = Planet(screen)
    sun = Sun(screen)
    asteroids = Group()
    stats = Stats()
    hp = Life(screen, stats)
    time = 0
    while True:
        time += 1
        Control.spawn(time, screen, asteroids)
        Control.events(sun)
        sun.update_sun()
        Control.update_asteroid(asteroids, sun, planet, stats, hp)
        Control.update(bg_menu, screen, asteroids, sun, planet, stats, hp, hearts)
        clock.tick(FPS)
        pygame.display.flip()
        if stats.life == 0:
            loose()
        if stats.life == 2:
            planet.image = pygame.image.load('images/Planet2.png')
        if stats.life == 1:
            planet.image = pygame.image.load('images/Planet3.png')
        print(sun.speed)


show_menu()
