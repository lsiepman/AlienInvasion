import sys
import pygame


def run_game():
    # Init game and create screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_colour = (24, 27, 97)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_colour)
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
