import pygame


class Particle:

    def __init__(self, screen, x, y, x_speed, y_speed, radius):
        self.screen = screen
        self.particles = []
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius

    def create_particle(self):
        self.particles.append([[self.x, self.y], [self.x_speed, self.y_speed], self.radius])

    def update_particle(self):
        for i, self.particle in reversed(list(enumerate(self.particles))):
            self.particle[0][0] += self.particle[1][0]
            self.particle[0][1] += self.particle[1][1]
            self.particle[2] -= 0.1

            reversed_particle = self.particle[len(self.particles) - i - 1]
            pygame.draw.circle(self.screen, (255, 255, 255), (int(reversed_particle[0][0]), int(reversed_particle[0][1])), reversed_particle[2])

            if self.particle[2] <= 0:
                self.particle.pop(i)