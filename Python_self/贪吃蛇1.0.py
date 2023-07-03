import pygame
import random

# 初始化游戏
pygame.init()

# 游戏区域大小
screen_width = 480
screen_height = 480

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("贪吃蛇")

# 创建时钟对象
clock = pygame.time.Clock()

# 定义蛇的初始位置和大小
snake_size = 10
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_speed_x = 0
snake_speed_y = 0
snake_body = []
snake_length = 1

# 定义食物的初始位置
food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

# 游戏循环标志位
game_over = False

# 游戏循环
while not game_over:

    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_speed_x = -snake_size
                snake_speed_y = 0
            elif event.key == pygame.K_RIGHT:
                snake_speed_x = snake_size
                snake_speed_y = 0
            elif event.key == pygame.K_UP:
                snake_speed_x = 0
                snake_speed_y = -snake_size
            elif event.key == pygame.K_DOWN:
                snake_speed_x = 0
                snake_speed_y = snake_size

    # 更新蛇的位置
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
        snake_length += 1

    # 更新蛇的身体
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # 检查蛇是否碰到自己或者边缘
    if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
        game_over = True
    for body in snake_body[:-1]:
        if body == snake_head:
            game_over = True

    # 绘制游戏画面
    screen.fill(black)
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
    for body in snake_body:
        pygame.draw
