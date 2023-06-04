import pygame
import sys
from bullet import Bullet
from vrag import Vrag
import time

def events(spaceship, screen, bullets):
     #обработка событий
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                spaceship.mright = True


            if event.key == pygame.K_a:
                spaceship.mleft = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet (screen, spaceship)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                spaceship.mright = False

            if event.key == pygame.K_a:
                spaceship.mleft = False

def update (bg_color, screen, spaceship, bullets, vragi):
    
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drow_bullet()
    spaceship.output()  
    vragi.draw(screen) 
    pygame.display.flip()

def update_bullets(bullets, vragi, screen):
    #удаление пуль за границей
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            #столкновение пуль
    collisions = pygame.sprite.groupcollide(bullets, vragi, True, True)
    if len(vragi) == 0:
        bullets.empty()
        army(screen, vragi)


def spaceship_death (stats, screen, spaceship, vragi, bullets):
      #столкновение корабля с врагами
        if stats.sokol_life > 0:
            stats.sokol_life -= 1
            vragi.empty()
            bullets.empty()
            army(screen, vragi)
            spaceship.create_spaceship()
            time.sleep(1)
        else:
        
            time.sleep(2)
            sys.exit()
    

def update_vragi(vragi, spaceship, screen, bullets, stats):
    #смещение врагов
    vragi.update()
    #столкновение
    if pygame.sprite.spritecollideany(spaceship, vragi):
        spaceship_death(stats, screen, spaceship, vragi, bullets)
    vragi_check(stats, screen, spaceship, vragi, bullets)

def vragi_check(stats, screen, spaceship, vragi, bullets):
    #выход за границы врагом
    screen_rect = screen.get_rect()
    for vrag in vragi.sprites():
        if vrag.rect.bottom >= screen_rect.bottom:
            spaceship_death(stats, screen, spaceship, vragi, bullets)
            break     

def army(screen, vragi):
    vrag = Vrag(screen)
    vrag_width = vrag.rect.width
    number_vrag_x = int((700 - 2 * vrag_width) / vrag_width)
    vrag_height = vrag.rect.height
    number_vrag_y = int((800 - 100 - 2 * vrag_height) / vrag_height)

    for row_number in range(number_vrag_y - 5):
    
        for vrag_number in range(number_vrag_x):
            vrag = Vrag(screen)
            vrag.x = vrag_width + vrag_width * vrag_number
            vrag.y = vrag_height + vrag_height * row_number
            vrag.rect.x = vrag.x
            vrag.rect.y = vrag.rect.height + (vrag.rect.height * row_number)
            vragi.add(vrag)