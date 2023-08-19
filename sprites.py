from cmath import rect
import pygame
import random
import math
from load_image import loadImage


class MasterSprite(pygame.sprite.Sprite):
    allSprites = None
    speed = None

class Death(MasterSprite):
    pool = pygame.sprite.Group()
    active = pygame.sprite.Group()
    
    def __init(self):
        super().__init__()
        self.image, self.rect = loadImage("dying.png", -1)
        self.linger = MasterSprite.speed * 3
    
    def position(cls, loc):
        if len(cls.pool) > 0:
            death = cls.pool.sprites()[0]
            death.add(cls.active, cls.allSprites)
            death.remove(cls.pool)
            death.rect.center = loc
            death.linger = 12
    
    def update(self):
        self.linger -= 1
        if self.linger <=0:
            self.remove(self.allsprtites, self.active)
            self.add(self.pool)

class Missile(MasterSprite):
    pool = pygame.sprite.Group()
    active = pygame.sprite.Group()

    def __init__(self):
        super().__init__()
        self.image, self.rect = loadImage("weapon.png", -1)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()

    def position(cls, loc):
        if len(cls.pool) > 0:
            missile = cls.pool.sprites()[0]
            missile.add(cls.allSprites, cls.active)
            missile.remove(cls.pool)
            missile.rect.midbottom = loc


