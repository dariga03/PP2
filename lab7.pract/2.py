import pygame

pygame.init()
pygame.display.set_mode((800, 300))


if done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


game.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))
game.display.flip()        