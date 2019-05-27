import sys
import pygame

def check_key_down(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_q:
        sys.exit(0)
def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_key_down(event,ship)
        elif event.type == pygame.KEYUP:
            check_key_up(event,ship)
def update_screen(ai_settings,screen,ship,alien,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
    pygame.display.flip()