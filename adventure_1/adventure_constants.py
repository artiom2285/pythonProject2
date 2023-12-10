import pygame

HEIGHT = 640
WIDTH = 896
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
JUMP_POWER = 7
GRAVITY = 0.35
PLATFORM = pygame.image.load("people/platf.png")
PLAYER = pygame.image.load("people/mario/0.png")
HEARTS = pygame.image.load("people/heart/1.png")

FIREBALL =  pygame.image.load("people/pngwing.com.png")

ANIMATION_DELAY = 100
ANIMATION_DELAY_ZOMBIE = 800
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"
GOLD = "#FFD700"
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
ANIMATION_JUMP_LEFT = [("people/mario/jl.png", 100)]
ANIMATION_JUMP_RIGHT = [("people/mario/jr.png", 100)]
ANIMATION_JUMP = [("people/mario/j.png", 100)]
ANIMATION_STAY = [("people/mario/0.png", 100)]
ANIMATION_FALL = [("people/mario/d.png", 100)]

BOSS_HELI_PIG = pygame.image.load("people/вертосвин.png")

MONSTERS_ANIM_LEFT = ["people/zombi/1.png",
                      "people/zombi/2.png",
                      "people/zombi/3.png",
                      "people/zombi/4.png",
                      "people/zombi/5.png",
                      "people/zombi/6.png",
                      "people/zombi/7.png",
                      "people/zombi/8.png",
                      "people/zombi/9.png",
                      "people/zombi/10.png",
                      "people/zombi/11.png",
                      "people/zombi/12.png",
                      "people/zombi/13.png",
                      "people/zombi/14.png",
                      "people/zombi/15.png",
                      "people/zombi/16.png",
                      "people/zombi/17.png",
                      "people/zombi/18.png",
                      ]

LEVEL = [
    "----------------------------",
    "-                          -",
    "-      +                   -",
    "-                          -",
    "-      --    ---           -",
    "-                          -",
    "-                --        -",
    "-                     -    *",
    "-            0      1      =",
    "-             --------------",
    "-                          -",
    "-       --                 -",
    "-            --            -",
    "-                          -",
    "-               -          -",
    "-                          -",
    "-   -                ---   -",
    "-   -                      -",
    "-   -           -          -",
    "-   -      ---             -",
    "-   - 1                    -",
    "-   ------------           -",
    "-                          -",
    "-                 -        -",
    "-                          -",
    "-              --          -",
    "-           --             -",
    "----------------------------"]
LEVEL_II = [
    "----------------------------------",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                *",
    "-                                =",
    "-                               --",
    "-          +                -    -",
    "-          --            --      -",
    "-                 --             -",
    "-                --              -",
    "-               ---              -",
    "-   -         --                 -",
    "-   -    --                      -",
    "-   -  1      1     0            -",
    "-   ----------------             -",
    "-                                -",
    "-                       --       -",
    "-                            --  -",
    "-                                -",
    "-                        --      -",
    "----------------------------------"]

LEVEL_III = [
    "----------------------------------",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "-                                -",
    "----------------------------------"]

LEVEL_III_COPY = [
    "----------------------------------",
    "-                                *",
    "-                                =",
    "-                   ----------   -",
    "-                                -",
    "-              -                 -",
    "-                 --------       -",
    "-                                -",
    "-                            --  -",
    "-                        --      -",
    "-                  -----         -",
    "-            --                  -",
    "-       ---                      -",
    "---                              -",
    "-                                -",
    "-    -------------               -",
    "-                      ---       -",
    "-                              ---",
    "-             +                  -",
    "----------------------------------"]