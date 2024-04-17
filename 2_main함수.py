import pygame
import os
import random
pygame.font.init()
pygame.init()


WIDTH, HEIGHT = 750, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # 보여지는 윈도우(화면)을 셋팅한다. 클라스
pygame.display.set_caption("Mygame")


# 이미지 로드
ENEMY_RED = pygame.image.load(
    os.path.join("image and sound", "enemy_red.png"))
ENEMY_YELLOW = pygame.image.load(
    os.path.join("image and sound", "enemy_green.png"))
ENEMY_PUPPLE = pygame.image.load(
    os.path.join("image and sound", "enemy_purple.png"))

# 플레이어 캐릭터
PLAYER_CHARACTER = pygame.image.load(
    os.path.join("image and sound", "player1.png"))
PLAYER_CHARACTER_1 = pygame.image.load(
    os.path.join("image and sound", "player1.png"))
PLAYER_CHARACTER_2 = pygame.image.load(
    os.path.join("image and sound", "player2.png"))
PLAYER_CHARACTER_3 = pygame.image.load(
    os.path.join("image and sound", "player3.png"))

# 레이져 이미지 로드
MISSILE_RED = pygame.image.load(
    os.path.join("image and sound", "enemy_red_missile.png"))
MISSILE_YELLOW = pygame.image.load(
    os.path.join("image and sound", "enemy_green_missile.png"))
MISSILE_PUPPLE = pygame.image.load(
    os.path.join("image and sound", "enemy_purple_missile.png"))

MISSILE_PLAYER = pygame.image.load(
    os.path.join("image and sound", "player1_missile.png"))
MISSILE_PLAYER_1 = pygame.image.load(
    os.path.join("image and sound", "player1_missile.png"))
MISSILE_PLAYER_2 = pygame.image.load(
    os.path.join("image and sound", "player2_missile.png"))
MISSILE_PLAYER_3 = pygame.image.load(
    os.path.join("image and sound", "player3_missile.png"))

# 배경
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("image and sound", "background_forest.png")), (WIDTH, HEIGHT))

bg_music = pygame.mixer.music.load(
    os.path.join("image and sound", "background_music.mp3"))
# pygame.mixer.music.play(-1)

missile_sound = pygame.mixer.Sound(
    os.path.join("image and sound", "missile_sound.wav"))

##############


def main():
    FPS = 60
    lost = False
    run = True
    clock = pygame.time.Clock()

    level = 0
    kill_score = 0

    main_font = pygame.font.SysFont("comicsans", 50)

    while run:
        clock.tick(FPS)
        WINDOW.blit(BG, (0, 0))

        level_label = main_font.render(f"Level : {level}", 1, (255, 255, 255))
        WINDOW.blit(level_label, (WIDTH-level_label.get_width()-10, 10))

        kill_label = main_font.render(
            f"Kill : {kill_score}", 1, (255, 255, 255))
        WINDOW.blit(kill_label, (kill_label.get_width()+40, 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


main()
