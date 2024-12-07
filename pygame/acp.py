import pygame
pygame.init()
win=pygame.display.set_mode((700,600))
pygame.display.set_caption("My first window screen")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()