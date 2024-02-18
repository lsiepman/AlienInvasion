import sys
from zoneinfo import available_timezones
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key in (pygame.K_RIGHT, pygame.K_d):
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


def update_screen(settings, screen, ship, aliens, bullets):
    "Update images on the screen and flip to the new screen"
    screen.fill(settings.bg_colour)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
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


def get_number_aliens(settings, alien_width):
    available_space_x = settings.screen_size[0] - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    "Determine the number of alien rows that fit on the screen"
    available_space_y = settings.screen_size[1] - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height)) - 4
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    "Create an alien and place it in the row"
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
    "Create a full fleet of aliens"
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens(settings, alien_width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)
