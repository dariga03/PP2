import pygame, time

clock = pygame.time.Clock()
 
pygame.init() 
W, H = 700 , 700
win = pygame.display.set_mode((W, H))
done = False

x, y = 350, 350

win.fill((255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                      
    press = pygame.key.get_pressed()
    if press[pygame.K_UP] and y > 20: y -= 20
    if press[pygame.K_DOWN] and y < H-20: y += 20
    if press[pygame.K_LEFT] and x > 20: x -= 20
    if press[pygame.K_RIGHT] and x < W-20: x += 20

    win.fill((255, 255, 255))
    
    pygame.draw.circle(win, (255, 0, 0), (x, y), 25)
        
    pygame.display.flip()
    clock.tick(60)