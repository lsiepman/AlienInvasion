import sys
import pygame
from settings import Settings


def run_game():

    # create instancce of settings class
    s = Settings()

    # Init game and create screen object
    pygame.init()
    screen = pygame.display.set_mode(s.screen_size)
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(s.bg_colour)
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
