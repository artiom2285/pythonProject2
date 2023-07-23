import pygame
import pyganim
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
        self.image.set_colorkey((136, 136, 136))
        self.go_left = []
        for anim in ANIMATION_LEFT:
            self.go_left.append((anim, ANIMATION_DELAY))
        self.anim_left = pyganim.PygAnimation(self.go_left)
        self.anim_left.play()
        self.go_right = []
        for anim2 in ANIMATION_RIGHT:
            self.go_right.append((anim2, ANIMATION_DELAY))
        self.anim_right = pyganim.PygAnimation(self.go_right)
        self.anim_right.play()
        self.anim_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.anim_jump_left.play()
        self.anim_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.anim_jump_right.play()
        self.jump_anim = pyganim.PygAnimation(ANIMATION_JUMP)
        self.jump_anim.play()
        self.stay_anim = pyganim.PygAnimation(ANIMATION_STAY)
        self.stay_anim.play()
        self.stay_anim.blit(self.image, (0, 0))

    def animation(self, pattern):
        self.anim = [pygame.image.load(i) for i in pattern]

    def update(self, platforms):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.speed = 5
            self.image.fill("#888888")
            if key[pygame.K_UP] or key[pygame.K_SPACE]:
                self.anim_jump_right.blit(self.image, (0, 0))
            else:
                self.anim_right.blit(self.image, (0, 0))
        elif key[pygame.K_LEFT]:
            self.speed = -5
            self.image.fill("#888888")
            if key[pygame.K_UP] or key[pygame.K_SPACE]:
                self.anim_jump_left.blit(self.image, (0, 0))
            else:
                self.anim_left.blit(self.image, (0, 0))
        else:
            self.speed = 0
            self.image.fill("#888888")
            self.stay_anim.blit(self.image, (0, 0))
        if key[pygame.K_UP] or key[pygame.K_SPACE]:
            if self.on_ground == True:
                self.speed_y -= JUMP_POWER
                self.image.fill("#888888")
                self.jump_anim.blit(self.image, (0, 0))
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