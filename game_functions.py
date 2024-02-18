import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, settings, screen, ship, bullets):
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

    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    ship.movement = False


def check_events(settings, screen, ship, bullets):
    "Respond to keypresses and mouse events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(settings, screen, ship, bullets):
    "Update images on the screen and flip to the new screen"
    screen.fill(settings.bg_colour)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    "Update bullet positions and remove old bullets"
    bullets.update()

    # remove bullets outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
