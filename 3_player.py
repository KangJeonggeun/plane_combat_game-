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


class Missile:
    pass


class Player:
    def __init__(self, x_pos, y_pos, hp):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.hp = hp

        self.player_img = PLAYER_CHARACTER
        self.missile_img = MISSILE_PLAYER

        self.missile_list = []
        self.mask = pygame.mask.from_surface(self.player_img)
        self.cooldown_counter = 0
        self.full_hp = 5

    def fire(self):
        if self.cooldown_counter == 0:
            missile = Missile(self.x_pos, self.y_pos, self.missile_img)
            self.missile_list.append(missile)
            self.cooldown_counter = 1

    def cooldown(self):
        if self.cooldown_counter >= 10:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def draw(self, window):
        self.cooldown()
        window.blit(self.player_img, (self.x_pos, self.y_pos))

        pygame.draw.rect(window, (255, 0, 0), (50, 35, 100, 20))
        pygame.draw.rect(window, (0, 0, 255), (50, 35, 100 *
                         (1-(self.full_hp-self.hp)/self.full_hp), 20))

        hp_title = pygame.font.SysFont(
            "comicsans", 30).render("HP", 1, (255, 255, 255))
        WINDOW.blit(hp_title, (0, 25))

    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()

    


def main():
    FPS = 60
    lost = False
    run = True
    clock = pygame.time.Clock()

    level = 0
    kill_score = 0

    player_vel = 7

    main_font = pygame.font.SysFont("comicsans", 50)

    player = Player(300, 630, 5)

    while run:
        clock.tick(FPS)
        WINDOW.blit(BG, (0, 0))

        level_label = main_font.render(f"Level : {level}", 1, (255, 255, 255))
        WINDOW.blit(level_label, (WIDTH-level_label.get_width()-10, 10))

        kill_label = main_font.render(
            f"Kill : {kill_score}", 1, (255, 255, 255))
        WINDOW.blit(kill_label, (kill_label.get_width()+40, 10))

        player.draw(WINDOW)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x_pos - player_vel > 0:
            player.x_pos -= player_vel
        if keys[pygame.K_RIGHT] and player.x_pos+player_vel + player.get_width() < WIDTH:
            player.x_pos += player_vel
        if keys[pygame.K_UP] and player.y_pos - player_vel > 0:
            player.y_pos -= player_vel
        if keys[pygame.K_DOWN] and player.y_pos+player_vel+player.get_height() < HEIGHT:
            player.y_pos += player_vel


main()
