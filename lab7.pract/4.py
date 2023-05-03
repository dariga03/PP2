import pygame
#import time


pygame.init()
screen = pygame.display.set_mode((800, 300))
done = False
is_blue = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue   

    #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 30, 40, 40))
    

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    #time.sleep(1/60)
    
    pygame.display.flip()        