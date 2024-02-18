import pygame
from pygame.sprite import Group
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
    ship = Ship(screen, s)

    # make bullets
    bullets = Group()

    while True:
        gf.check_events(s, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(s, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
