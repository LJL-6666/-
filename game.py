# 0 - 模块区
import datetime
import math
import os
import random
import sys

import pygame
from pygame.locals import *


class Begger(object):
    def __init__(self, img, rect, speed):
        self.ful_img = img
        self.imgs = [self.ful_img.subsurface(Rect((i*83, 0), (83, 93)))
                     for i in range(3)]
        self.rect = rect
        self.speed = speed
        self.num = 0

    def update(self, screen, press_keys):
        if press_keys[K_a]:
            self.rect.left -= self.speed
            if self.rect.left <= 0:
                self.rect.left = 0
        if press_keys[K_d]:
            self.rect.left += self.speed
            if self.rect.right >= 200:
                self.rect.right = 200
        if press_keys[K_w]:
            self.rect.top -= self.speed
            if self.rect.top <= 0:
                  self.rect.top = 0
        if press_keys[K_s]:
            self.rect.top += self.speed
            if self.rect.bottom >= 640:
                  self.rect.bottom = 640
        self.num += 1
        if self.num % 3 == 0:
            self.num = 0
        return [(self.rect.left + self.rect.right)/2, (self.rect.top + self.rect.bottom)/2], self.imgs[self.num]


# 主要的工作区域
if __name__ == '__main__':

    # 1 - 设置区

    # 1.1 - 窗口设置区
    white = (255, 255, 255)
    screen_width, screen_height = 960, 640
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pas_Game")

    # 1.2 - 基础设置区
    pygame.init()

    start = 0
    win = 0
    running = 0

    distance = 200
    health_value = 194
    health_value_max = 194
    fin_time = 90
    start_time = datetime.datetime.now()

    rect_bg = Rect(50, 50, 133, 142)
    bg_speed = 2
    begger_pos = []

    monsters = []
    monster_speed = 2

    wave_set = []
    wave_speed = 3.0
    wave_max = 20

    fig_path = r'C:\Users\ASUS\Desktop\pack/'
    paper = pygame.image.load(fig_path + 'paper.png').convert_alpha()

    wall = pygame.image.load(fig_path + 'walls.png').convert_alpha()
    wall_width = wall.get_width()
    wall_height = wall.get_height()

    begger = pygame.image.load(fig_path + 'beggers.png').convert_alpha()
    begger_width = begger.get_width()
    begger_height = begger.get_height()

    waves = pygame.image.load(fig_path + 'waves.png').convert_alpha()
    sub_wave = waves.subsurface(Rect((0, 0), (waves.get_width() / 5, waves.get_height())))
    sub_wave_width = sub_wave.get_width()
    sub_wave_height = sub_wave.get_height()

    monster_img1 = pygame.image.load(fig_path + 'monster1.PNG').convert_alpha()#
    monster_width = monster_img1.get_width()
    monster_height = monster_img1.get_height()
    monster_img = monster_img1

    health_bar_img = pygame.image.load(fig_path + "health_bar.png")
    health_bar_height = health_bar_img.get_height()

    health_img = pygame.image.load(fig_path + "health.png")
    health_height = health_img.get_height()

    victory = pygame.image.load(fig_path + 'victory.png')
    game_over = pygame.image.load(fig_path + 'game_over.png')

    start_img = pygame.image.load(fig_path + 'start.png').convert_alpha()

    # 2 - 游戏区
    while not start:
        screen.fill(white)
        screen.blit(start_img, (160, 0))
        pygame.font.init()
        font = pygame.font.Font(None, 84)
        text = font.render("Press Space to Start !",
                           True, (250, 50, 200))
        text_Rect = text.get_rect()
        text_Rect.centerx = screen.get_rect().centerx
        text_Rect.centery = screen.get_rect().centery + 200
        screen.blit(text, text_Rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    start = 1
                    running = 1
                    pygame.mixer.music.load(fig_path + "Checkpoint.mp3")
                    pygame.mixer.music.play(1, 0.0)
                    pygame.mixer.music.set_volume(0.15)
                    start_time = datetime.datetime.now()

    bg = Begger(begger, rect_bg, bg_speed)
    # 2.2 - 游戏进行区
    while running:
        # 2.2.1 - 游戏显示区
        screen.fill(white)
        screen.blit(paper, (0, 0))
        for height in range(0, screen_height, wall_height):
            screen.blit(wall, (distance, height))

        press_keys = pygame.key.get_pressed()
        begger_pos, begger_img = bg.update(screen, press_keys)

        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (begger_pos[1] + begger_height),
                           position[0] - (begger_pos[0] + begger_width))
        begger_rot = pygame.transform.rotate(begger_img, 360 - angle * 57.29)
        begger_pos1 = (begger_pos[0] - begger_rot.get_rect().width / 2,
                       begger_pos[1] - begger_rot.get_rect().height / 2)
        screen.blit(begger_rot, begger_pos1)

        for wave in wave_set:
            index = 0
            vel_x = math.cos(wave[0]) * wave_speed
            vel_y = math.sin(wave[0]) * wave_speed
            wave[1] += vel_x
            wave[2] += vel_y
            if wave[1] < - sub_wave_width or wave[1] > screen_width \
                    or wave[2] < - sub_wave_height or wave[2] > screen_height:
                wave_set.pop(index)
            index += 1
            for projectile in wave_set:
                wave1 = pygame.transform.rotate(sub_wave, 360 - projectile[0] * 57.29)
                screen.blit(wave1, (projectile[1], projectile[2]))
        monster_timer = random.choice(range(200))
        if monster_timer < 1:
            monsters.append([screen_width,
                             random.randint(monster_height, screen_height - monster_height)])
        index = 0

        for monster in monsters:
            if monster[0] < - monster_width:
                monsters.pop(index)
            monster[0] -= monster_speed
            monster_rect = pygame.Rect(monster_img.get_rect())
            monster_rect.top = monster[1]
            monster_rect.left = monster[0]
            if monster_rect.left < wall_width + distance:
                health_value -= random.randint(20, 50)
                monsters.pop(index)
            index1 = 0
            for wave in wave_set:
                wave_rect = pygame.Rect(sub_wave.get_rect())
                wave_rect.left = wave[1]
                wave_rect.top = wave[2]
                # 检查两个矩形块是否交叉
                if monster_rect.colliderect(wave_rect):
                    wave_set.pop(index1)
                    try:
                        monsters.pop(index)
                    except IndexError as error:
                        print("IndexError: " + str(error))
                index1 += 1
            index += 1

        for monster in monsters:
            screen.blit(monster_img, monster)

        font = pygame.font.Font(None, 42)
        cur_time = datetime.datetime.now()
        play_time = (cur_time - start_time).seconds
        if play_time % 60 < 10:
            time_str = ":0"
        else:
            time_str = ":"
        survived_text = font.render(
            str(play_time // 60) +
            time_str +
            str(play_time % 60),
            True, (0, 0, 0)
        )
        text_Rect = survived_text.get_rect()
        text_Rect.topright = [screen_width - 5, 5]
        screen.blit(survived_text, text_Rect)

        health_bar_img = pygame.transform.scale(health_bar_img,
                                                (health_value_max, health_bar_height))
        screen.blit(health_bar_img, [0, 5])

        if health_value < 0:
            health_value = 0
        health_img = pygame.transform.scale(health_img,
                                            (health_value, health_height))
        screen.blit(health_img, [0, 5])

        pygame.display.flip()

        # 2.2.2 - 游戏操作区
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and len(wave_set) < wave_max:
                position = pygame.mouse.get_pos()
                wave_set.append([math.atan2(position[1] - (begger_pos1[1] + begger_height),
                                            position[0] - (begger_pos1[0] + begger_width)),
                                 begger_pos1[0], begger_pos1[1]])

        if pygame.time.get_ticks() >= fin_time * 1000:
            running = 0
            win = 1
        if health_value == 0:
            running = 0
            win = 0

    while not running and start:

        pygame.mixer.music.stop()
        if win:
            screen.blit(victory, (100, 0))
            pygame.font.init()
            font = pygame.font.Font(None, 84)
            text = font.render("Victory !",
                               True, (250, 50, 200))
            text_Rect = text.get_rect()
            text_Rect.centerx = screen.get_rect().centerx + 10
            text_Rect.centery = screen.get_rect().centery + 50
            screen.blit(text, text_Rect)
        if not win:
            screen.blit(game_over, (100, 0))
            pygame.font.init()
            font = pygame.font.Font(None, 100)
            text = font.render("GAME OVER",
                               True, (250, 50, 200))
            text_Rect = text.get_rect()
            text_Rect.centerx = screen.get_rect().centerx 
            text_Rect.centery = screen.get_rect().centery + 80
            screen.blit(text, text_Rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
