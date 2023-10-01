import pygame
from adventure_constants import *
from player import Player
from platform import Platform, Door, Key
from camera import Camera
from monsters import Zombies


def draw_level(level):
    for y, row in enumerate(level):
        for x, item in enumerate(row):
            if item == "-":
                pf = Platform(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(pf)
                platforms.append(pf)
                platforms_group.add(pf)
            elif item == "*":
                door = Door(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                door_list.append(door)
                entities.add(door)
                door_group.add(door)
            elif item == "+":
                key = Key(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(key)
                key_group.add(key)
            elif item =="1":
                zombie = Zombies(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT + 10)
                entities.add(zombie)
                zombie_group.add(zombie)
                zombie_list.append(zombie)

def camera_config(camera, target_rect):
    x, y, _, _ = target_rect
    _, _, w, h = camera
    left = - x + WIDTH // 2
    right = - y + HEIGHT // 2
    left = max(-(camera.width - WIDTH), min(0, left))
    right = min(0, max(-(camera.height - HEIGHT), right))
    return pygame.Rect(left, right, w, h)
pygame.init()
running = True
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Artiom and Vova's adventure")
bg = pygame.Surface((900, 640))
bg.fill("#004400")
platforms = []
zombie_list = []
door_list = []
timer = pygame.time.Clock()
player = Player(55, WIDTH -400)
entities = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
entities.add(player)
total_level_width = len(LEVEL[0]) * PLATFORM_WIDTH
total_level_height = len(LEVEL) * PLATFORM_HEIGHT
camera = Camera(camera_config, total_level_width, total_level_height)
players = pygame.sprite.Group()
players.add(player)
door_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
current_level = LEVEL
draw_level(level=LEVEL)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    window.blit(bg, (0, 0))
    next_level = pygame.sprite.groupcollide(door_group, players, False, False)
    if next_level:
        if player.key == True:
            total_level_width = len(LEVEL_II[0]) * PLATFORM_WIDTH
            total_level_height = len(LEVEL_II) * PLATFORM_HEIGHT
            camera.new_level(total_level_width, total_level_height)
            player.rect.center = (55, WIDTH -400)
            platforms = []
            for pf in platforms_group:
                pf.kill()
            for dr in door_group:
                dr.kill()
            for zomb in zombie_group:
                zomb.kill()
            draw_level(LEVEL_II)
    damage = pygame.sprite.groupcollide(zombie_group, players, False, False)
    if damage:
        if player.get_damage():
            player.kill()
    get_key = pygame.sprite.groupcollide(key_group, players, True, False)
    if get_key:
        player.key = True
        for door in door_list:
            door.set_image()
    entities.update(platforms, zombie_list)
    camera.update(player)
    for e in entities.sprites()[:: -1]:
        window.blit(e.image, camera.apply(e))
    player.draw_lives(window)
    pygame.display.update()
    timer.tick(60)

pygame.quit()