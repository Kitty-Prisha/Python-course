import pygame
import random
pygame.init()
spritecolor=pygame.USEREVENT+1
bgcolor=pygame.USEREVENT+2
#background colors
blue=pygame.color("blue")
lightblue=pygame.color("lightblue")
darkblue=pygame.color("darkblue")
#sprite color
yellow=pygame.color("yellow")
red=pygame.color("red")
green=pygame.color("green")
orange=pygame.color("orange")
class sprite(pygame.sprite.Sprite)
    def __init__(self,color,height,width):
        super.__init__()
        self.image=pygame.Surface([height,width])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        
