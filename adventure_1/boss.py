import pygame
from adventure_constants import *
import random


class BossHeliPig(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = BOSS_HELI_PIG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hp = 500
        self.max_hp = 500
        self.timer = 600
        self.timer2 = 200
        self.speed_x = 3
        self.speed_y = 3
        self.name = "Helipig"

    def update(self, platforms, *args, **kwargs):
        if self.timer2 > 0:
            self.timer2 -= 1
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if self.rect.x > platform.rect.x and self.rect.y > 32 and self.rect.bottom < 608:
                    self.speed_x = random.randint(1, 6)
                    self.image_copy = self.image.copy()
                    self.image = pygame.transform.flip(self.image_copy, True, False)
                    self.rect.x += 8
                elif self.rect.x < platform.rect.x and self.rect.y > 32 and self.rect.bottom < 608:
                    self.speed_x = random.randint(-6, -1)
                    self.image_copy = self.image.copy()
                    self.image = pygame.transform.flip(self.image_copy, True, False)
                    self.rect.x -= 8
                if self.rect.bottom > 608:
                    self.speed_y = random.randint(-6, -1)
                elif self.rect.top < 32:
                    self.speed_y = random.randint(1, 6)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def get_damage(self):
        if self.timer2 == 0:
            self.timer2 = 200
            self.hp -= 50
            if self.hp == 0:
                return 1
            return 2