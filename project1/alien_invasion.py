'''
@Author: your name
@Date: 2020-02-20 17:35:46
@LastEditTime: 2020-02-24 19:06:30
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
from alien import Alien


'''
@description: 计算屏幕宽度可以容纳多少个外星人
@param {type} 
@return: 可以容纳的外星人数量
'''
def get_number_alien_x(ai_settings,alien_width):
    availabel_space_x = ai_settings.screen_width - 2*alien_width #屏幕空间用来放置外星人　屏幕左右两边不放
    number_aliens_x = int(availabel_space_x/(2*alien_width))+1#每隔一个外星人放置一个
    return number_aliens_x

'''
@description: 计算距离飞船可以容纳的外星人的行数
@param {type} 
@return: 可以容纳的外星人数量
'''
def get_number_alien_y(ai_settings,ship_height,alien_heigth):
    available_space_y = (ai_settings.screen_height-(3*alien_heigth)-ship_height)
    number_rows = int(available_space_y/(2*alien_heigth))
    return number_rows
    


'''
@description: 创建外星人群
@param {ai_settings}:计算屏幕的宽度可以容纳多少外星人
@param {screen}: 给到屏幕
@param {aliens} : 存储外星人群的变量
@return: 
'''
def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_alien_y = get_number_alien_y(ai_settings,ship.rect.height,alien.rect.height)+1

    for y_number in range(number_alien_y):
        for x_number in range(number_alien_x):
            alien = Alien(ai_settings,screen)
            alien_width = alien.rect.width
            alien.x = alien_width+ 2*alien_width*x_number #计算每一个外星人的坐标 公差为２个外星人的宽度 an = a1 + (n-1)*d
            alien.rect.x = alien.x

            alien.rect.y = alien.rect.height+2*alien.rect.height*y_number
            
            aliens.add(alien)
        


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
    aliens = Group() #　存放外星人的group
    create_fleet(ai_settings,screen,ship,aliens)# 创建外星人群
   
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
        
        for alien in aliens:
            alien.bliteme()

        pygame.display.flip()# 绘制屏幕


run_game()