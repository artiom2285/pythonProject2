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
        self.animation()
        self.lives = 3
        self.timer = 0
        self.move = None
        self.key = False

    def animation(self):
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
        self.fall_anim = pyganim.PygAnimation(ANIMATION_FALL)
        self.fall_anim.play()
        self.stay_anim.blit(self.image, (0, 0))

    def update(self, platforms, zombie_list, **kwargs):
        if self.timer > 0:
            key = None
            self.timer -= 1
            for zombi in zombie_list:
                damage = pygame.sprite.collide_rect(zombi, self)
                if damage:
                    if self.rect.left < zombi.rect.left and self.rect.right < zombi.rect.right:
                        self.move = "left"
                    elif self.rect.right > zombi.rect.right and self.rect.right > zombi.rect.right:
                        self.move = "right"
            if self.move == "left":
                self.speed = -3
            elif self.move == "right":
                self.speed = 3
        else:
            self.move = None
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] or key[pygame.K_SPACE]:
                if self.on_ground == True:
                    self.speed_y -= JUMP_POWER
                    self.on_ground = False
                self.image.fill("#888888")
                self.jump_anim.blit(self.image, (0, 0))
            if key[pygame.K_RIGHT]:
                self.speed = 5
                self.image.fill("#888888")
                if key[pygame.K_UP] or key[pygame.K_SPACE]:
                    if self.on_ground == True:
                        self.speed_y -= JUMP_POWER
                    self.anim_jump_right.blit(self.image, (0, 0))
                else:
                    self.anim_right.blit(self.image, (0, 0))
            elif key[pygame.K_LEFT]:
                self.speed = -5
                self.image.fill("#888888")
                if key[pygame.K_UP] or key[pygame.K_SPACE]:
                    if self.on_ground == True:
                        self.speed_y -= JUMP_POWER
                    self.anim_jump_left.blit(self.image, (0, 0))
                else:
                    self.anim_left.blit(self.image, (0, 0))
            if not (key[pygame.K_RIGHT] or key[pygame.K_LEFT]):
                self.speed = 0
                if not (key[pygame.K_UP] or key[pygame.K_SPACE]):
                    self.image.fill("#888888")
                    self.stay_anim.blit(self.image, (0, 0))
        self.on_ground = False
        self.speed_y += GRAVITY
        if self.speed_y > GRAVITY * 3:
            self.image.fill("#888888")
            self.fall_anim.blit(self.image, (0, 0))
        self.rect.x += self.speed
        self.callide(self.speed, 0, platforms)
        self.rect.y += self.speed_y
        self.callide(0, self.speed_y, platforms)

    def draw_lives(self, window):
        x_pos = 20

        for _ in range(self.lives):
            window.blit(HEARTS, (x_pos, 20))
            x_pos += 64

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

    def get_damage(self):
        if self.timer == 0:
            self.timer = 60
            self.lives -= 1
            if self.lives == 0:
                return 1
            return 2