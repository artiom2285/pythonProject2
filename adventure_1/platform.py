import pygame
from adventure_constants import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image = PLATFORM

class Platf_for_zomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image.fill("#004400")

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, down = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image = pygame.image.load("people/door.png")
        if down:
            self.image = self.image.subsurface(pygame.Rect(0, 32, PLATFORM_WIDTH, PLATFORM_HEIGHT))
        else:
            self.image = self.image.subsurface(pygame.Rect(0, 0, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    def set_image(self):
        self.image.fill("#ffffff")

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("people/key.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)