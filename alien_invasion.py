import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
# 创建一个显示窗口
#       self.screen = pygame.display.set_mode((1200, 800)) 如果不用settings.py
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion Game for Gavin")
        self.ship = Ship(self)
#       self.bg_color = (230,230,230)  如果不用settings.py
# 这个游戏由方法run_game()控制。该方法包含一个不断运行的while循环，而这个循环包含一个事件循环以及管理屏幕更新的代码。
# 事件是用户玩游戏时执行的操作，如按键或移动鼠标。为程序响应事件，可编写一个事件循环，以侦听事件并根据发生的事件类型执行合适的任务。
# for循环就是一个事件循环。
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()    # 加入以便每次执行循环时都调用飞船的方法update()
            self._update_screen()
# flip()让最近绘制的屏幕可见。在这里，它在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。
# 我们移动游戏元素时，flip()将不断更新屏幕，以显示元素的新位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果。
            pygame.display.flip()  # display.flip() will update the contents of the entire display.
                                   # display.update() allows to update a portion of the screen,

# 辅助方法在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以单个下划线打头。
# These methods are only meant to be called from within the class, isn’t meant for public use
    def _check_events(self):
        for event in pygame.event.get():
            # if event.type == pygame.quit()  you are actually executing the quit() function before pygame is initialized.
            # In the second you are comparing the event to the event named QUIT.
            # 当玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
            if event.type == pygame.QUIT:  #or event.type == pygame.K_q:
                sys.exit()
#每当用户按键时，都将在Pygame中注册一个事件。事件都是通过方法pygame.event.get()获取的，因此需要在方法_check_events()中指定要检查哪些类型的事件。
#每次按键都被注册为一个KEYDOWN事件。
            elif event.type ==pygame.KEYDOWN:
                 self._check_keydown_events(event)   #响应按键，重构了函数_check_keydown_events从此处分离
            elif event.type ==pygame.KEYUP:          # pygame.KEYUP事件，以便知道玩家何时松开右箭头键
                 self._check_keyup_events(event)     #松开按键，重构了函数_check_keyup_events从此处分离

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:  # 向右移动飞船
            # self.ship.rect.x +=1
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # 向zuo移动飞船
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

if __name__ =='__main__':  # 仅当直接运行该文件时，它们才会执行
    ai = AlienInvasion()
    ai.run_game()
