'''
@Author: your name
@Date: 2020-02-22 00:17:39
@LastEditTime: 2020-02-22 00:44:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python/learnpython3/project1/bullit.py
'''
import pygame
from pygame.sprite import Sprite # Sprite 简单的游戏对象类

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect( # 子弹并非是图片　所以要自己创建一个Rect
            0,0,ai_settings.bullet_width,ai_settings.bullet_height)  
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor