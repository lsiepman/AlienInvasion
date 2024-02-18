import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():

    # create instancce of settings class
    settings = Settings()

    # Init game and create screen object
    pygame.init()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(settings)

    # make a ship
    ship = Ship(screen, settings)

    # make bullets
    bullets = Group()

    # make aliens
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # draw stars
    stars = Group()
    gf.decorate_sky(settings, screen, stars)

    # make play button
    play_button = Button(settings, screen, "Play")

    while True:
        gf.check_events(settings, screen, stats, play_button, ship, bullets)
        gf.update_screen(
            settings, stats, screen, ship, aliens, bullets, stars, play_button
        )
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
