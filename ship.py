import pygame

class Ship:
# 接受两个参数：引用self和指向当前AlienInvasion实例的引用。这让Ship能够访问AlienInvasion中定义的所有游戏资源。
    def __init__(self,ai_game):
# 初始化飞船并且设置其初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # 引入在setting.py里的速度值
        self.screen_rect = ai_game.screen.get_rect()   # 使用方法get_rect()访问屏幕的属性rect. Get error when enter "self.screen.rect = "

# 加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

# 对于每搜新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

# 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

# 移动标志
        self.moving_right = False
        self.moving_left = False

# 根据移动标志调整飞船位置。需要注意用的是两个if，而不是elif,原因见书P
    def update(self):  #根据移动标志调整飞机位置,更新飞船而不是rect对象的x值
        if  self.moving_right and self.rect.right < self.screen_rect.right:  #向右移动且没到达屏幕右边缘,防止飞船飞出屏幕
#           self.rect.x +=1    # Before把speed放入setting.py中
            self.x +=self.settings.ship_speed
        if  self.moving_left and self.rect.left>0:                        # 向左移动，且rect左边缘的坐标大于零，就说明飞船未触及屏幕左边缘，,防止飞船飞出屏幕
#           self.rect.x -=1     # Before把speed放入setting.py中
            self.x -=self.settings.ship_speed
#根据self.x 更新rect对象
        self.rect.x = self.x

# 定义了方法blitme()，它将图像绘制到self.rect指定的位置。
    def blitme(self):
        self.screen.blit(self.image,self.rect)