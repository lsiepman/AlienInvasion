import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        self.score_image = self.font.render(
            f"score: {self.stats.score}",
            True,
            self.text_colour,
            self.settings.bg_colour,
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.high_score_image = self.font.render(
            f"high score: {int(self.stats.high_score)}",
            True,
            self.text_colour,
            self.settings.bg_colour,
        )

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        self.level_image = self.font.render(
            f"level: {int(self.stats.level)}",
            True,
            self.text_colour,
            self.settings.bg_colour,
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        "Show how many ships are left"
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
