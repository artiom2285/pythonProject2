import pygame
from adventure_constants import *


class Camera:
    def __init__(self, camera_funk, width, height):
        self.camera_funk = camera_funk
        self.state = pygame.Rect(0, 0, (width, height))