import pygame
from adventure_constants import *
from player import Player
from platform import Platform


def draw_level(level):
    for y, row in enumerate(level):
        for x, item in enumerate(row):
            if item == "-":
                pf = Platform(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(pf)
                platforms.append(pf)
pygame.init()
running = True
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Artiom and Vova's adventure 1")
bg = pygame.Surface((900, 640))
bg.fill("#004400")

timer = pygame.time.Clock()
player = Player(55, WIDTH -400)
entities = pygame.sprite.Group()
platforms = []
entities.add(player)
draw_level(level=LEVEL)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    window.blit(bg, (0, 0))

    player.update(platforms)
    entities.draw(window)
    pygame.display.update()
    timer.tick(60)

pygame.quit()