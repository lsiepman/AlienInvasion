class GameStats:
    "Keep track of game statistics"

    def __init__(self, settings):
        "Initialise stats"
        self.settings = settings
        self.reset_stats()
        self.high_score = 0

        # start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.settings.initialise_dynamic_settings()
        self.score = 0
        self.level = 1
