import pygame


pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 30, 40, 40))
    #time.sleep(1000)
    pygame.display.flip()        