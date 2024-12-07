import pygame
pygame.init()
window=pygame.display.set_mode((500,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(window,(100,45,78),pygame.Rect(100, 200, 100, 200))
    pygame.display.flip()
            