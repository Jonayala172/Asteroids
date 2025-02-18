import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        new_angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = self.velocity.rotate(new_angle) * 1.2

        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = self.velocity.rotate(-new_angle) * 1.2

        self.kill()
