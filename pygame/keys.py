import pygame
def main():
    pygame.init()
    screen_width, screen_height=500,500
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('color changing sprite')
    colors={
        'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'yellow':pygame.Color('yellow'),
        'blue':pygame.Color('blue'),
        'white':pygame.Color('white'),
    }
    current=colors['white']
    x,y=30,30
    spriteh,spritew=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3
        x=min(max(0,x),screen_width-spritew)
        y=min(max(0,x),screen_height-spriteh)
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current,(x,y,spritew,spriteh))
        pygame.display.flip()
    pygame.quit()
if __name__== "__main__":
    main()
