
import pygame,sys
from pygame.locals import *
pygame.init() #初始化pygame模块
DISPLAYSURF = pygame.display.set_mode((400,300)) #长400，宽300
pygame.display.set_caption('Hello World SBSB!')
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,128)
 
fontObj = pygame.font.Font('freesansbold.ttf',32)
#render方法返回Surface对象
textSurfaceObj = fontObj.render('Hello world!',True,GREEN,BLUE)
#get_rect()方法返回rect对象
textRectObj = textSurfaceObj.get_rect()
textRectObj.center=(200,150)
 
while True:
	DISPLAYSURF.fill(BLACK)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

