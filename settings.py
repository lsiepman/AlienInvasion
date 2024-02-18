class Settings:
    "A class to store global Alien Invasion settings"

    def __init__(self) -> None:
        # Screen settings
        self.screen_size = (1400, 750)
        self.bg_colour = (24, 27, 97)

        # ship settings
        self.ship_speed_factor = 1

        # bullet settings
        self.bullet_speed_factor = self.ship_speed_factor * (2 / 3)
        self.bullet_size = (3, 15)
        self.bullet_colour = (201, 178, 62)
        self.bullets_allowed = 7
