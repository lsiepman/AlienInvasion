import sys
import pygame


def check_events():
    "Respond to keypresses and mouse events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    "Update images on the screen and flip to the new screen"
    screen.fill(settings.bg_colour)
    ship.blitme()
    pygame.display.flip()
