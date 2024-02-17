import pygame


class Ship:

    def __init__(self, screen, settings) -> None:
        "Init ship and starting position"
        self.screen = screen
        self.ship_settings = settings

        image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(image, (30, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        # movement flag
        self.movement = False
        self.direction = None

    def blitme(self) -> None:
        "Draw the ship at its current location"
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movement:
            if self.direction == "R" and self.rect.right < self.screen_rect.right:
                self.center1 += self.ship_settings.ship_speed_factor

            elif self.direction == "L" and self.rect.left > 0:
                self.center1 -= self.ship_settings.ship_speed_factor

            elif self.direction == "U" and self.rect.top > 0:
                self.center2 -= self.ship_settings.ship_speed_factor

            elif self.direction == "D" and self.rect.bottom < self.screen_rect.bottom:
                self.center2 += self.ship_settings.ship_speed_factor

        self.rect.centerx = self.center1
        self.rect.centery = self.center2
