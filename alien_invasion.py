import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    # create instancce of settings class
    s = Settings()

    # Init game and create screen object
    pygame.init()
    screen = pygame.display.set_mode(s.screen_size)
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    while True:
        gf.check_events()
        gf.update_screen(s, screen, ship)


if __name__ == "__main__":
    run_game()
