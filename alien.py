import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    "A class to represent a single alien"

    def __init__(self, settings, screen):
        "Initialise the alien and set its starting position"
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image
        image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(image, (50, 30))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        "Draw the alien at its current location"
        self.screen.blit(self.image, self.rect)
