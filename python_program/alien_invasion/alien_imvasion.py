import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ai_ship=Ship(screen)
    bg_color=ai_settings.bg_color
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ai_ship)

run_game()