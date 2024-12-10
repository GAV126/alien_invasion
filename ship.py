import pygame

class Ship:
# 接受两个参数：引用self和指向当前AlienInvasion实例的引用。这让Ship能够访问AlienInvasion中定义的所有游戏资源。
    def __init__(self,ai_game):
# 初始化飞船并且设置其初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()   # 使用方法get_rect()访问屏幕的属性rect. Get error when enter "self.screen.rect = "

# 加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

# 对于每搜新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

# 移动标志
        self.moving_right = False
        self.moving_left = False
# 根据移动标志调整飞船位置
# 需要注意用的是两个if，而不是elif
    def update(self):
        if self.moving_right:
            self.rect.x +=1
        if self.moving_left:
            self.rect.x -=1
# 定义了方法blitme()，它将图像绘制到self.rect指定的位置。
    def blitme(self):
        self.screen.blit(self.image,self.rect)