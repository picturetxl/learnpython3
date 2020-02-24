'''
@Author: your name
@Date: 2020-02-24 17:52:52
@LastEditTime: 2020-02-24 19:50:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /learnpython3/project1/alien.py
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image,(70,70)) # 放大缩小图像
        self.rect = self.image.get_rect()
        
        self.rect.x = 10
        self.rect.y = 10
        self.x = float(self.rect.x) #记录alien的位置

        
            
       
        
                

    def bliteme(self):# 绘制alien
        self.screen.blit(self.image,self.rect)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:#如果外星人的右边线的位置大于屏幕右边线的位置
            return True
        elif self.rect.left <=0:#外星人的左边线的位置小于０
            return True
        