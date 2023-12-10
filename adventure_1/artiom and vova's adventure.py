import pygame
from adventure_constants import *
from player import Player
from platform import Platform, Door, Key, Platf_for_zomb
from camera import Camera
from monsters import Zombies
from boss import BossHeliPig
from weapons import FireBall
from explosion import Explosion


def draw_level(level):
    global platforms
    global pf_for_zomb
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera.new_level(total_level_width, total_level_height)
    player.rect.center = (55, WIDTH - 400)
    platforms = []
    pf_for_zomb = []
    for pf in platforms_group:
        pf.kill()
    for pfzombie in invis_pf_group:
        pfzombie.kill()
    for dr in door_group:
        dr.kill()
    for zomb in zombie_group:
        zomb.kill()
    door_list.clear()
    if num_level in boss_level:
        create_boss(num_level)
    for y, row in enumerate(level):
        for x, item in enumerate(row):
            if item == "-":
                pf = Platform(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(pf)
                platforms.append(pf)
                platforms_group.add(pf)
            elif item == "*" or item == "=":
                if item == "*":
                    door = Door(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                else:
                    door = Door(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT, "down")
                door_list.append(door)
                entities.add(door)
                door_group.add(door)
                platforms.append(door)
            elif item == "+":
                key = Key(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(key)
                key_group.add(key)
            elif item == "1":
                zombie = Zombies(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT + 10)
                entities.add(zombie)
                zombie_group.add(zombie)
                zombie_list.append(zombie)
            elif item == "0":
                pfzomb = Platf_for_zomb(x * PLATFORM_WIDTH, y * PLATFORM_HEIGHT)
                entities.add(pfzomb)
                pf_for_zomb.append(pfzomb)
                invis_pf_group.add(pfzomb)

def draw_hp(screen, x, y, hp, hp_width, hp_height, boss):
    rect = pygame.Rect(x, y, hp_width, hp_height)
    fill = (hp / boss.max_hp) * hp_width
    fill_rect = pygame.Rect(x, y, fill, hp_height)
    pygame.draw.rect(screen, "#ff0000", fill_rect)
    pygame.draw.rect(screen, "#ffffff", rect, 1)

def draw_text(screen, x, y, size, text, color):
    font_name = "people/font.ttf"
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)

def camera_config(camera, target_rect):
    x, y, _, _ = target_rect
    _, _, w, h = camera
    left = - x + WIDTH // 2
    right = - y + HEIGHT // 2
    left = max(-(camera.width - WIDTH), min(0, left))
    right = min(0, max(-(camera.height - HEIGHT), right))
    return pygame.Rect(left, right, w, h)

def create_boss(num_level):
    global boss
    boss = boss_level.get(num_level)
    boss = boss(WIDTH // 2, HEIGHT - 100)
    entities.add(boss)
    boss_group.add(boss)

def get_hit_sprite(hit_dict):
    for hit in hit_dict.values():
        return hit[0]

pygame.init()
running = True
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Artiom and Vova's adventure")
bg = pygame.Surface((900, 640))
bg.fill("#004400")
platforms = []
zombie_list = []
door_list = []
pf_for_zomb = []
boss_level = {3:BossHeliPig}
timer = pygame.time.Clock()
player = Player(55, WIDTH -400)
entities = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
invis_pf_group = pygame.sprite.Group()
entities.add(player)
camera = Camera(camera_config, 32, 32)
players = pygame.sprite.Group()
players.add(player)
door_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
fireball_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
num_level = 1
boss = None
boss_attack = 180

current_level = LEVEL
draw_level(level=LEVEL)
levels = {1: LEVEL_II, 2: LEVEL_III, 3:LEVEL_III_COPY}
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
            current_level = levels.get(num_level)
            num_level += 1
            draw_level(current_level)
    damage = pygame.sprite.groupcollide(zombie_group, players, False, False)
    if damage:  #столкновение с зомби
        y = player.get_damage()
        if y == 1:
            player.kill()
    get_key = pygame.sprite.groupcollide(key_group, players, True, False)
    if get_key:
        player.key = True
        for door in door_list:
            door.set_image()
            platforms.remove(door)
    entities.update(platforms, zombie_list, pf_for_zomb = pf_for_zomb)
    camera.update(player)
    for e in entities.sprites()[:: -1]:
        window.blit(e.image, camera.apply(e))
    if num_level in boss_level:
        draw_hp(window, WIDTH - 220, 50, boss.hp, 200, 20, boss)
        draw_text(window, WIDTH - 120, 40, 40, boss.name, WHITE)
        boss_attack -= 1
        if boss_attack <= 0 and boss.hp > 0:
            fireball = FireBall(boss.rect)
            entities.add(fireball)
            fireball_group.add(fireball)
            boss_attack = 180
        elif boss.hp <= 0:
            for fire in fireball_group:
                explosion = Explosion(fire.rect.center)
                entities.add(explosion)
                fire.kill()
            current_level = levels.get(num_level)
            num_level += 1
            draw_level(current_level)
        damage = pygame.sprite.groupcollide(players, fireball_group, False, False)
        if damage:
            y = player.get_damage()
            if y == 1:
                ball = get_hit_sprite(damage)
                explosion = Explosion(ball.rect.center)
                entities.add(explosion)
                ball.kill()
                player.kill()
            elif y == 2:
                ball = get_hit_sprite(damage)
                explosion = Explosion(ball.rect.center)
                entities.add(explosion)
                ball.kill()
        damage_boss = pygame.sprite.groupcollide(boss_group, fireball_group, False, False)
        if damage_boss:
            s = boss.get_damage()
            if s == 1:
                ball = get_hit_sprite(damage_boss)
                explosion = Explosion(ball.rect.center)
                entities.add(explosion)
                ball.kill()
                boss.kill()
            elif s == 2:
                ball = get_hit_sprite(damage_boss)
                explosion = Explosion(ball.rect.center)
                entities.add(explosion)
                ball.kill()
    player.draw_lives(window)
    pygame.display.update()
    timer.tick(60)
pygame.quit()