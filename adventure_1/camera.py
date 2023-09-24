import pygame
from adventure_constants import *


class Camera(pygame.sprite.Sprite):
    def __init__(self, camera_funk, widt, heigh):
        pygame.sprite.Sprite.__init__(self)
        self.camera_funk = camera_funk
        self.state = pygame.Rect(0, 0, widt, heigh)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_funk(self.state, target.rect)

    def new_level(self, widt, heigh):
        self.state = pygame.Rect(0, 0, widt, heigh)