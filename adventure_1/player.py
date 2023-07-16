import pygame
from adventure_constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed_y = 0
        self.on_ground = False
        self.speed = 0
        self.start_x = x
        self.start_y = y
        self.image = pygame.Surface((22, 32))
        self.image.fill("#888888")
        self.rect = pygame.Rect(x, y, 22, 32)
        self.image = PLAYER

    def update(self, platforms):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.speed = 5
        elif key[pygame.K_LEFT]:
            self.speed = -5
        else:
            self.speed = 0
        if key[pygame.K_UP] or key[pygame.K_SPACE]:
            if self.on_ground == True:
                self.speed_y -= JUMP_POWER
        self.on_ground = False
        self.speed_y += GRAVITY
        self.rect.x += self.speed
        self.callide(self.speed, 0, platforms)
        self.rect.y += self.speed_y
        self.callide(0, self.speed_y, platforms)

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def callide(self, x, y, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if x > 0:
                    self.rect.right = platform.rect.left
                if x < 0:
                    self.rect.left = platform.rect.right
                if y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.speed_y = 0
                if y < 0:
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0