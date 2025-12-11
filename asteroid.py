import random
import pygame
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            reflection_angle = random.uniform(20, 50)
            deflect_angle_1 = self.velocity.rotate(reflection_angle) * 1.2
            deflect_angle_2 = self.velocity.rotate(-reflection_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_1.velocity = deflect_angle_1
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_2.velocity = deflect_angle_2
            
         