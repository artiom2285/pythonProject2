import pygame
from adventure_constants import *
from pygame.math import Vector2
import random


class FireBall(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = FIREBALL
        self.rect = pygame.Rect(*position.center, 40, 40)
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.speed_x = 7
        self.speed_y = 7

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)
        #self.rect.update(self.rect.x, self.rect.y, 40, 40)

    def update(self, platforms, *args, **kwargs):
        self.rotate(15)
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if self.rect.x > platform.rect.x and self.rect.y > 32 and self.rect.bottom < 608:
                    self.speed_x = random.randint(7, 7)
                    self.image_copy = self.image.copy()
                    self.image = pygame.transform.flip(self.image_copy, True, False)
                    self.rect.x += 8
                elif self.rect.x < platform.rect.x and self.rect.y > 32 and self.rect.bottom < 608:
                    self.speed_x = random.randint(-7, -7)
                    self.image_copy = self.image.copy()
                    self.image = pygame.transform.flip(self.image_copy, True, False)
                    self.rect.x -= 8
                if self.rect.bottom > 608:
                    self.speed_y = random.randint(-6, -1)
                elif self.rect.top < 32:
                    self.speed_y = random.randint(1, 6)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y