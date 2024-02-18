import sys
from random import randint
import pygame
from bullet import Bullet
from alien import Alien
from star import Star


def check_events(settings, screen, ship, bullets):
    "Respond to keypresses and mouse events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


# Keyboard functions
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


# update functions
def update_screen(settings, screen, ship, aliens, bullets, stars):
    "Update images on the screen and flip to the new screen"
    screen.fill(settings.bg_colour)
    stars.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(settings, screen, ship, aliens, bullets):
    "Update bullet positions and remove old bullets"
    bullets.update()
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)


def update_aliens(settings, ship, aliens):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")


# bullet functions
def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # remove bullets outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)


# alien functions
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


def check_fleet_edges(settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


# star functions
def get_max_star_rows(settings, star_height):
    return int(settings.screen_size[1] / (randint(7, 14) * star_height))


def get_max_star_cols(settings, star_width):
    return int(settings.screen_size[0] / (randint(7, 14) * star_width))


def create_star(settings, screen, stars):
    "Create an alien and place it in the row"
    star = Star(settings, screen)
    star_width = star.rect.width
    star.x = star_width + randint(0, settings.screen_size[0] - star_width)
    star.rect.x = star.x
    star.rect.y = star.rect.height + randint(
        0, settings.screen_size[0] - star.rect.height
    )
    stars.add(star)


def decorate_sky(settings, screen, stars):
    "Create a full fleet of aliens"
    star = Star(settings, screen)
    number_stars_x = get_max_star_cols(settings, star.rect.width)
    number_rows = get_max_star_rows(settings, star.rect.height)

    for _ in range(number_rows):
        for _ in range(number_stars_x):
            create_star(settings, screen, stars)
