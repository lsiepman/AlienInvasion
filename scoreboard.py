import pygame.font


class Scoreboard:

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()

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

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)