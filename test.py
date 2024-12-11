# import sys, pygame
# pygame.init()
#
# size = width, height = 320, 240
# speed = [1, 1]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load('images/ship.bmp')
# ballrect = ball.get_rect()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()

# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Hello World")
# while True:
#    for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          pygame.quit()
#          sys.exit()
#       if event.type == pygame.MOUSEBUTTONDOWN:
#          pos=pygame.mouse.get_pos()
#          btn=pygame.mouse
#          print ("x = {}, y = {}".format(pos[0], pos[1]))


x = 3
y = 10

if x > y:
    print("x is greater than y.")

print("do nothing")