import pygame


HEIGHT = 640
WIDTH = 896
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
JUMP_POWER = 7
GRAVITY = 0.35
PLATFORM = pygame.image.load("people/platf.png")
PLAYER = pygame.image.load("people/player.png")
LEVEL = [
       "----------------------------",
       "-                          -",
       "-                          -",
       "-       --                 -",
       "-            --            -",
       "-                          -",
       "-               -          -",
       "-                          -",
       "-                   ---    -",
       "-                          -",
       "-      ---      -          -",
       "-                          -",
       "---                        -",
       "-   ------------           -",
       "-                          -",
       "-                -         -",
       "-                          -",
       "-              --          -",
       "-           --             -",
       "----------------------------"]