import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    "A class to represent a single star"

    def __init__(self, settings, screen):
        "Initialise the star and set its  position"
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image
        image = pygame.image.load("images/star.bmp")
        self.image = pygame.transform.scale(image, (10, 10))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        "Draw the star at its current location"
        self.screen.blit(self.image, self.rect)
