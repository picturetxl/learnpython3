'''
@Author: your name
@Date: 2020-02-20 17:35:46
@LastEditTime: 2020-02-22 00:55:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python/project1/alien_invasion.py
'''

from settings import Settings # 游戏的全局设置
from ship import Ship #　飞船
from bullet import Bullet # 子弹类
import sys # 用来退出游戏
import pygame
from pygame.sprite import Group # 

'''
@description: run game
@param {type} 
@return: 
'''
def run_game():

    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    
    ship = Ship(ai_settings,screen)
    bullets = Group() # Group 存放是sprite的游戏对象
    
    #　游戏主循环
    while True:
        #　监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT:窗口的关闭按钮
                sys.exit()
            elif event.type == pygame.KEYDOWN: # 按下事件
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(ai_settings,screen,ship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP: # 抬起事件
                 if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                 elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
            
            
        if ship.moving_right and ship.rect.right < screen.get_rect().right:
            ship.center += ai_settings.ship_speed_factor
        if ship.moving_left and ship.rect.left > screen.get_rect().left:
            ship.center -= ai_settings.ship_speed_factor

        # 绘制飞船
        ship.rect.centerx = ship.center
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 绘制子弹
        for bullet in bullets.sprites():
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
                continue
            bullet.y -= bullet.speed_factor # 计算子弹的ｙ方向的位置
            bullet.rect.y = bullet.y # 更新子弹这个Rect的位置
            pygame.draw.rect(bullet.screen,bullet.color,bullet.rect)
            

        pygame.display.flip()# 绘制屏幕


run_game()