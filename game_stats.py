class GameStats:
    "Keep track of game statistics"

    def __init__(self, settings):
        "Initialise stats"
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
