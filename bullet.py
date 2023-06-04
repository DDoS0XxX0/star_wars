import pygame
from pygame.sprite import Group

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, spaceship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 199, 21, 133
        self.speed = 1.5
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def drow_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)