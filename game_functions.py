import sys
import pygame


def check_keydown_events(event, ship):
    if event.key in (pygame.K_RIGHT, pygame.K_d):
        ship.movement = True
        ship.direction = "R"

    elif event.key in (pygame.K_LEFT, pygame.K_a):
        ship.movement = True
        ship.direction = "L"

    elif event.key in (pygame.K_UP, pygame.K_w):
        ship.movement = True
        ship.direction = "U"

    elif event.key in (pygame.K_DOWN, pygame.K_s):
        ship.movement = True
        ship.direction = "D"


def check_keyup_event(event, ship):
    ship.movement = False


def check_events(ship):
    "Respond to keypresses and mouse events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(settings, screen, ship):
    "Update images on the screen and flip to the new screen"
    screen.fill(settings.bg_colour)
    ship.blitme()
    pygame.display.flip()
