'''
@Author: your name
@Date: 2020-02-20 18:09:16
@LastEditTime: 2020-02-24 18:23:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python/project1/ship.py
'''

import pygame
'''
@description:ship 
@param {screen:飞船贴在指定的surface 上} 
@return: 
'''
class Ship():
    def __init__(self,ai_settings,screen):
        # 背景屏幕－－母版
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ai_settings  =ai_settings
        self.image = pygame.image.load("images/spaceship.png") # 飞船的样子
        self.image = pygame.transform.scale(self.image,(200,200)) # 放大缩小图像
        self.rect = self.image.get_rect() #飞船的尺寸
        self.moving_right = False
        self.moving_left = False
        # 飞船的位置 -- 一开始的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image,self.rect)