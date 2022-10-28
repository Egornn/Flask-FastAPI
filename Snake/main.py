import pygame
import time

pygame.init()

# Initial var
size_x = 640
size_y = 480
is_lost = False

# Snake default head coordinates
x_0 = size_x / 2
y_0 = size_y / 2
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
color_msg = red

# x,y change
x_upd = 0
y_upd = 0
step = 1
speed = 150

dis = pygame.display.set_mode((size_x, size_y))

def UpdateBoard (dis, x_0, y_0):
    dis.fill(white)
    pygame.draw.rect(dis, green, [x_0, y_0, 10, 10])
    pygame.display.update()

def IsGameOver (x, y):
    global size_x, size_y
    if x<=0 or x>=size_x or y<=0 or y>=size_y : return True
    else: return False

def Alert (message):
    global color_msg, dis
    msg = pygame.font.SysFont(None, 45).render(message, True, color_msg)
    dis.blit(msg, [dis.get_height()*5/11, dis.get_width()/3])

def GameLoop():
    global x_0, y_0,x_upd, y_upd, step, is_lost, speed, dis
    timer = pygame.time.Clock()
    pygame.display.update()
    pygame.display.set_caption('Ssssnake')
    while not is_lost:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                is_lost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x_upd = 0
                    y_upd = step
                elif event.key == pygame.K_UP:
                    x_upd = 0
                    y_upd = -step
                elif event.key == pygame.K_RIGHT:
                    x_upd = step
                    y_upd = 0
                elif event.key == pygame.K_LEFT:
                    x_upd = -step
                    y_upd = 0
        x_0 += x_upd
        y_0 += y_upd
        UpdateBoard(dis, x_0, y_0)
        is_lost=IsGameOver(x_0,y_0)
        timer.tick(speed)
    Alert("You have lost")
    pygame.display.update()
    time.sleep(5)




GameLoop()
pygame.quit()
quit()
