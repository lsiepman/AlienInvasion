import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    "A class to manage bullets"

    def __init__(self, settings, screen, ship):
        "Create a bullet object at ship's current position"
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_size[0], settings.bullet_size[1])
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.colour = settings.bullet_colour
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        "Move bullets up the screen"
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
