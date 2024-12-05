import pygame
pygame.init()
window=pygame.display.set_mode((500,600))
pygame.display.set_caption("Making a window using pygame")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
background_image=pygame.transform.scale(pygame.image.load('student.png').convert(),(500,600))            
pygame.display.flip()
            
