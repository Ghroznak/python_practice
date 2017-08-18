import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
#background=pygame.image.load('bg.png')

BLACK = 0,0,0
UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('images/skull50x50.png')
spritex=200
spritey=130
direction=DOWN


#pygame.mixer.music.load('bgm.mp3')
#pygame.mixer.music.play(-1, 0.0)
while True:
    #DISPLAYSURF.blit(BLACK,(0,0))

	DISPLAYSURF.blit(sprite,(spritex,spritey))

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

	if event.type == KEYDOWN:
		if (event.key == K_LEFT):
			spritex-=5
			DISPLAYSURF.fill(BLACK)
			DISPLAYSURF.blit(sprite,(spritex,spritey))
		elif(event.key == K_LEFT and event.key == K_UP):
			spritex-=3
			spritey-=3
			DISPLAYSURF.fill(BLACK)
			DISPLAYSURF.blit(sprite,(spritex,spritey))
		elif (event.key == K_RIGHT):
			spritex+=5
			DISPLAYSURF.fill(BLACK)
			DISPLAYSURF.blit(sprite,(spritex,spritey))
		elif (event.key == K_UP):
			spritey-=5
			DISPLAYSURF.fill(BLACK)
			DISPLAYSURF.blit(sprite,(spritex,spritey))
		elif (event.key == K_DOWN):
			spritey+=5
			DISPLAYSURF.fill(BLACK)
			DISPLAYSURF.blit(sprite,(spritex,spritey))
		
	pygame.display.flip()
	fpsClock.tick(FPS)