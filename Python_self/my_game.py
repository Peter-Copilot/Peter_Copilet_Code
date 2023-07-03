import pygame
from pygame import locals
import random

pygame.init()  # 初始化
# 创建一个窗口
class Block(pygame.sprite.Sprite):
    def __init__(self,image1,image2,image3):
        super().__init__()
        self.image=random.choice([image1,image2,image3])
        self.rect=self.image.get_rect()
        self.rect.x=1000
        self.rect.y=500-self.rect.height
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=150
        self.rect.y=400
screen = pygame.display.set_mode((1000, 600))
FPS = pygame.time.Clock()  # pygame时钟，控制游戏速度（帧数）
pygame.display.set_caption("悟空酷跑")
# 载入图片
background = pygame.image.load('bg.png')    # 背景
road = pygame.image.load('road.png')      # 路
stone = pygame.image.load('stone.png')      # 石头
cacti = pygame.image.load('cacti.png')      # 仙人掌
bush = pygame.image.load('bush.png')      # 灌木丛
hero = [pygame.image.load('hero1.png'),
        pygame.image.load('hero2.png'),
        pygame.image.load('hero3.png'),
        pygame.image.load('hero4.png'),
        pygame.image.load('hero5.png')]
index = 0   
time=0
y = 400
jumpState = "runing"
t = 30
obstacle = Block(bush,stone,cacti)
block_list = pygame.sprite.Group()
block_list.add(obstacle)
road_x=0
background_x=0
gamestate=True

while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == locals.KEYDOWN:
            if jumpState == "runing":
                if event.key == locals.K_SPACE:
                    jumpState = "up"
    # 悟空造型
    wukong = Player(hero[index])
    if jumpState == "runing":       # 跑步状态下
        index += 1
        if index >= 5:
            index = 0

    if jumpState == "up":    # 起跳状态
        if t > 0:
            y -= t
            wukong.rect.y=y
            t -= 2
        else:
            jumpState = "down"  
    if jumpState == "down":    # 降落状态
        if t <= 30:
            y += t
            wukong.rect.y=y
            t += 2
        else:
            jumpState = "runing"
            t =30
    
    
    

    if gamestate==True:# 将背景图画上去
        background_x-=2
        if background_x<=-1000:
            background_x=0
        screen.blit(background, (background_x, 0))     # 远处背景
        road_x-=8
        if road_x<=-1000:
            road_x=0
        screen.blit(road, (road_x, 500))     # 路
        screen.blit(wukong.image, (150, y))     # 悟空


        time+=1
        if time>=60:
            time=0
            num=random.randint(0,50)
            if num>20:
                obstacle=Block(bush,cacti,stone)
                block_list.add(obstacle)
        for sprite in block_list:
            sprite.rect.x-=10
            screen.blit(sprite.image,(sprite.rect.x,sprite.rect.y))
            if sprite.rect.x<=0-sprite.rect.width:
                sprite.kill()
            if pygame.sprite.collide_rect(wukong,sprite):
                gameover=pygame.image.load('gameover.png')
                screen.blit(gameover,(400,200))
                gamestate=False


    screen.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y)) 
    # 刷新画面
    pygame.display.update()
    FPS.tick(60)