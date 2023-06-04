import pygame
import control
from spaceship import Spaceship
from pygame.sprite import Group
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Звездные Войны:)")
    bg_color = (0, 0, 0)
    spaceship = Spaceship(screen)
    bullets = Group()
    vragi = Group()
    control.army(screen, vragi)
    stats = Stats()

    while True:
           
        control.events(spaceship, screen, bullets)
        if stats.run_game:
            spaceship.update_spaceship()
            control.update(bg_color, screen, spaceship, bullets, vragi)
            control.update_bullets(bullets, vragi, screen)
            control.update_vragi(vragi, spaceship, screen, bullets, stats)
run()       