'''
@Author: your name
@Date: 2020-02-20 17:58:46
@LastEditTime: 2020-02-24 20:17:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python/project1/settings.py
'''

class Settings():
    def __init__(self):
        # 整个屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        
        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        # 外星人的设置
        self.alien_speed_factor = 1 #移动速度
        self.fleet_drop_speed = 12
        self.fleet_dicrection = 1#１:right -1: left
        

