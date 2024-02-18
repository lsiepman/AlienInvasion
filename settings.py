class Settings:
    "A class to store global Alien Invasion settings"

    def __init__(self) -> None:
        # Screen settings
        self.screen_size = (1400, 750)
        self.bg_colour = (24, 27, 97)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_size = (3, 15)
        self.bullet_colour = (201, 178, 62)
        self.bullets_allowed = 7

        # alien settings
        self.fleet_drop_speed = 10

        # game settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = self.ship_speed_factor * 3
        self.alien_speed_factor = self.ship_speed_factor / 3
        self.fleet_direction = 1  # 1 = right, -1 = left
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
