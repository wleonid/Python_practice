import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ai_ship=Ship(ai_settings,screen) 
    alien = Alien(ai_settings,screen)
    while True:
        gf.check_events(ai_ship)
        ai_ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ai_ship,alien,bullets)
run_game()