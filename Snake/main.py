import pygame
import time
import random

pygame.init()

# Initial var
size_x = 640
size_y = 480

# Snake default head coordinates

green = (0, 255, 0)
white = (222, 222, 222)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
color_msg = red
font = pygame.font.SysFont("comicSans", 26)
font_ui = pygame.font.SysFont("comicSans", 30)

# x,y change

step = 20
speed = 10
snake_tough = 20
x_upd = step
y_upd = 0

dis = pygame.display.set_mode((size_x, size_y))
pygame.display.update()
pygame.display.set_caption('Ssssnake')


def snake_body(size, snake_parts):
    global snake_tough, dis
    for block in snake_parts:
        pygame.draw.rect(dis, green, [block[0], block[1], size, size])
    pygame.display.update()


def UpdateBoard(dis, x_0, y_0, food_x, food_y):
    global snake_tough
    dis.fill(white)
    pygame.draw.rect(dis, green, [x_0, y_0, snake_tough, snake_tough])
    pygame.draw.rect(dis, blue, [food_x, food_y, snake_tough, snake_tough])
    pygame.display.update()


def IsGameOver(x, y, snake_parts):
    global size_x, size_y
    if x <= 0 or x >= size_x or y <= 0 or y >= size_y or [x, y] in snake_parts[:-1]:
        return True
    else:
        return False



def Alert(message):
    global color_msg, dis, font
    msg = font.render(message, True, color_msg)
    dis.blit(msg, [dis.get_height() / 10, dis.get_width() / 3])


def GameLoop():
    global x_upd, y_upd, step, speed, dis, snake_tough
    is_lost = False
    is_close = False
    x_0 = size_x / 2
    y_0 = size_y / 2
    snake_parts = []
    snake_length = 1
    timer = pygame.time.Clock()
    food_x = random.randint(snake_tough, size_x - snake_tough) // snake_tough * snake_tough
    food_y = random.randint(snake_tough, size_y - snake_tough) // snake_tough * snake_tough
    print(x_0, y_0, food_x, food_y)
    while not is_lost:
        while is_close:
            dis.fill(white)
            Alert("You have lost. Press R to restart or Q to exit")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        is_close = False
                        is_lost = True
                    elif event.key == pygame.K_r:
                        GameLoop()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                is_lost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and not (x_upd == 0 and y_upd == -step):
                    x_upd = 0
                    y_upd = step
                elif event.key == pygame.K_UP and not (x_upd == 0 and y_upd == step):
                    x_upd = 0
                    y_upd = -step
                elif event.key == pygame.K_RIGHT and not (x_upd == -step and y_upd == 0):
                    x_upd = step
                    y_upd = 0
                elif event.key == pygame.K_LEFT and not (x_upd == step and y_upd == 0):
                    x_upd = -step
                    y_upd = 0
        x_0 += x_upd
        y_0 += y_upd
        snake_head = []
        snake_head.append(x_0)
        snake_head.append(y_0)
        snake_parts.append(snake_head)
        if snake_length < len(snake_parts):
            del snake_parts[0]
        for block in snake_parts[:-1]:
            if block == snake_head:
                is_close = True
        if x_0 == food_x and y_0 == food_y:
            food_x = random.randint(snake_tough, size_x - snake_tough) // snake_tough * snake_tough
            food_y = random.randint(snake_tough, size_y - snake_tough) // snake_tough * snake_tough
            snake_length += 1
        UpdateBoard(dis, x_0, y_0, food_x, food_y)
        snake_body(snake_tough, snake_parts)
        value = font_ui.render(f"Score: {str(snake_length-1)}", True, red)
        dis.blit(value, [0, 0])
        pygame.display.update()
        is_close = IsGameOver(x_0, y_0, snake_parts)
        timer.tick(speed)


GameLoop()
pygame.quit()
quit()
