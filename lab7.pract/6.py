import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False
white = [255, 255, 255]
screen.fill(white)
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

#pressed = pygame.key.get_pressed()
#       if pressed[pygame.K_UP]: y -= 5
#        if pressed[pygame.K_DOWN]: y += 5
#        if pressed[pygame.K_LEFT]: x -= 5
#        if pressed[pygame.K_RIGHT]: x += 5 

up_pressed = pygame.get_pressed()
    if pressed[pygame.K_UP]: y -=5                 
          

    pygame.draw.circle(screen, (255, 0, 0) , (x, y), 25)
    pygame.display.flip()        
