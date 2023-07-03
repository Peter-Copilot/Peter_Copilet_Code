import pygame
import random
from pygame import locals

record = 0

# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((660, 480))

# 背景
background = pygame.image.load('bg.png')
right = pygame.image.load('right.png')
food = pygame.image.load('apple.png')
body = pygame.image.load('body.png')
left = pygame.image.load('left.png')
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')


snake_x , snake_y = 240 , 120


BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)

shengcheng = True

chaoxiang = 'right'
chaoxiang_1 = right
FPSCLOOK = pygame.time.Clock()

xy_tanchishe = [(180,90), (180,120), (210,120), (snake_x, snake_y)]

while True:
    
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render('Hello world!',True,GREEN,BLUE)
#get_rect()方法返回rect对象
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center=(200,150)
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == locals.KEYDOWN:
            #print(1)
            if event.key == locals.K_RIGHT and chaoxiang != 'left':
                chaoxiang = 'right'
                chaoxiang_1 = right
            if event.key == locals.K_LEFT and chaoxiang != 'right':
                chaoxiang = 'left'
                chaoxiang_1 = left
            if event.key == locals.K_DOWN and chaoxiang != 'up':
                chaoxiang = 'down'
                chaoxiang_1 = down
            if event.key == locals.K_UP and chaoxiang != 'down':
                chaoxiang = 'up'
                chaoxiang_1 = up
    if chaoxiang == 'right':
        snake_x += 30
    elif chaoxiang == 'left':
        snake_x -= 30
    elif chaoxiang == 'up':
        snake_y -= 30
    else:
        snake_y += 30

    xy_tanchishe.append((snake_x,snake_y))
    xy_tanchishe.pop(0)
    # 将背景图画上去
    screen.blit(background, (0, 0))
    # 将贪吃蛇头画上去
    screen.blit(chaoxiang_1, (snake_x, snake_y))
    # 将贪吃蛇的身体画上去
    for i in range(len(xy_tanchishe)-1):
        screen.blit(body,xy_tanchishe[i])

    # screen.blit(body, (210, 120))
    # screen.blit(body, (180, 120))
    # screen.blit(body, (180, 90))
    # 将果实画上去
    #screen.blit(food, (random.randint(30, 650), random.randint(30, 450)))
    if shengcheng:
        shengcheng_x = random.randrange(30, 620, 30)
        shengcheng_y = random.randrange(30, 450, 30)
        shengcheng = False
        
    screen.blit(food, (shengcheng_x, shengcheng_y))  
    
    if snake_x == shengcheng_x and snake_y == shengcheng_y:
        shengcheng = True

        xy_tanchishe.insert(0, xy_tanchishe[0])
        
        record += 1
    
    if snake_x < 0 or snake_x > 660 or snake_y < 0 or snake_y > 480:
        print('分数：', record)
        exit()   
         
    FPSCLOOK.tick(3)
        
    

    # 刷新画面
    pygame.display.update()