import pygame
import pyganim
from adventure_constants import *
import copy


class Zombies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -1
        self.monsters_anim()
        self.direction = "left"

    def monsters_anim(self):
        self.go_left2 = []
        for image in MONSTERS_ANIM_LEFT:
            image = pygame.transform.scale(pygame.image.load(image), (PLATFORM_WIDTH, PLATFORM_HEIGHT + 8))
            self.go_left2.append((image, ANIMATION_DELAY))
        self.anim_left = pyganim.PygAnimation(self.go_left2)
        self.anim_right = pyganim.PygAnimation(self.go_left2)
        self.anim_right.flip(True, False)
        self.anim_left.play()
        self.anim_right.play()

    def update(self, platforms: list, *args, **kwargs):
        platforms = copy.copy(platforms)
        platforms.extend(kwargs["pf_for_zomb"])
        self.rect.x += self.speed
        self.callide(platforms)
        if self.direction == "left":
            self.image.fill("#004400")
            self.anim_left.blit(self.image, (0, 0))
        elif self.direction == "right":
            self.image.fill("#004400")
            self.anim_right.blit(self.image, (0, 0))

    def callide(self, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if self.direction == "right":
                    self.direction = "left"
                    self.speed = -1
                    self.rect.right = platform.rect.left - 2
                elif self.direction == "left":
                    self.direction = "right"
                    self.speed = 1
                    self.rect.left = platform.rect.right + 1