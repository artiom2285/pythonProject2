import pygame


HEIGHT = 640
WIDTH = 896
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
JUMP_POWER = 7
GRAVITY = 0.35
PLATFORM = pygame.image.load("people/platf.png")
PLAYER = pygame.image.load("people/mario/0.png")
ANIMATION_DELAY = 100
ANIMATION_RIGHT = [
       "people/mario/r1.png",
       "people/mario/r2.png",
       "people/mario/r3.png",
       "people/mario/r4.png",
       "people/mario/r5.png",
]
ANIMATION_LEFT = [
       "people/mario/l1.png",
       "people/mario/l2.png",
       "people/mario/l3.png",
       "people/mario/l4.png",
       "people/mario/l5.png",
]
ANIMATION_JUMP_LEFT = [("people/mario/jl.png",100)]
ANIMATION_JUMP_RIGHT = [("people/mario/jr.png",100)]
ANIMATION_JUMP = [("people/mario/j.png",100)]
ANIMATION_STAY = [("people/mario/0.png",100)]
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