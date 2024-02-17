import pygame


class Ship:

    def __init__(self, screen) -> None:
        "Init ship and starting position"
        self.screen = screen
        image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(image, (40, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self) -> None:
        "Draw the ship at its current location"
        self.screen.blit(self.image, self.rect)
