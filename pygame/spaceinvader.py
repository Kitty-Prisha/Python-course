import pygame
import random
import math
screenwidth=800
screenheight=500
playerstartX=370
playerstartY=380
enemystartymin=50
enemystartymax=150
enemyspeedx=4
enemyspeedy=40
collisiondistance=27
pygame.init()
screen=pygame.display.set_mode(screenwidth,screenheight)
background=pygame.image.load('spacebg.png')
player=pygame.image.load('player.png')
enemy=pygame.image.load('enemy.png')
ufo=pygame.image.load('ufo.png')
bullet=pygame.image.load('bullet.png')
pygame.display.set_caption("Space invader")
pygame.display.set_icon(ufo)
playerimg=[]
playerx=playerstartX
playery=playerstartY
playerchange=0
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numofenemy=6
for _i in range(numofenemy):
    enemyimg.append(enemy)
    enemyx.append(random.randint(0,screenwidth-64))
    enemyy.append(random.randint(enemystartymin,enemystartymax))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)
    





