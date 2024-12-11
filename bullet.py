import pygame
from pygame.sprite import  Sprite

class Bullet(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings =ai_game.settings
        self.colour = self.settings.bullet_colour

# 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
# 创建子弹的属性rect。子弹并非基于图像，因此必须使用pygame.Rect()类从头开始创建一个矩形。
# 创建这个类的实例时，必须提供矩形左上角的坐标和坐标，以及矩形的宽度和高度
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  # 将子弹的rect.midtop设置为飞船的rect.midtop。这样看起来像是从飞船中射出的

        self.y = float(self.rect.y)


# 向上移动子弹，更新表示子弹位置的小数值。
    def update(self):
        self.y-=self.settings.bullet_speed     # 子弹向上移动，意味着其坐标将不断减小。为更新子弹的位置，从self.y中减去settings
        self.rect.y=self.y                     # 更新表示子弹的rect的位置。

# 在屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.colour,self.rect)