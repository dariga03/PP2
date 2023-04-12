import pygame
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (221, 160, 221)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


pygame.display.set_caption('PAINT')
screen.fill(WHITE)

R = 30 #radius

img = pygame.transform.scale(pygame.image.load('paint.jpeg'), (150, 150))  #новый размер изображении
points = []

def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def drawPolygon(color, points):
    pygame.draw.polygon(screen, color, points, 4)  

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, R, 4)

def eraser(pos):
    pygame.draw.circle(screen, WHITE, pos, R)



finished = False
drawing = False

color = pygame.Color('black')


start_pos = 0
end_pos = 0
shape = 0


while not finished:
    clock.tick(60)

    
    pos = pygame.mouse.get_pos() #cursor

    screen.blit(img, (10, 10)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos 
            if pos[0]>10 and pos[0]<160 and pos[1]>10 and pos[1]<160:
                color = screen.get_at(pos)

        if event.type==pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos

            #rectangle
            rect_x=abs(start_pos[0]-end_pos[0])  
            rect_y=abs(start_pos[1]-end_pos[1])         

            #circle
            circ_x=abs(start_pos[0]+rect_x//2)          
            circ_y=abs(start_pos[1]+rect_y//2)

            #triangle
            tr1 = (start_pos[0], start_pos[1])
            tr2 = (end_pos[0], end_pos[1])
            tr3 = (start_pos[0], start_pos[1]+rect_y)

            #rombus 
            a = ((start_pos[0]+rect_x//2), start_pos[1])
            b = ((start_pos[0]+rect_x), (start_pos[1]+rect_y//2))
            c = ((end_pos[0]-rect_x//2), end_pos[1])
            d = (start_pos[0], (start_pos[1]+rect_y//2))

            #equilateral triangle
            etr_a = (start_pos[0], start_pos[1]+rect_x)
            etr_b = (start_pos[0]+rect_x, start_pos[1]+rect_x)
            etr_c = (start_pos[0]+rect_x//2, start_pos[1])

            if shape == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            if shape == 1:
                drawCircle(color, (circ_x, circ_y), rect_x//2)
            if shape == 2:
                drawRect(color, start_pos, rect_x, rect_x)
            if shape == 3:  
                points = [a, b, c, d]
                drawPolygon(color, points)
            if shape == 4: 
                points = [tr1, tr2, tr3]
                drawPolygon(color, points)
            if shape == 5:  
                points = [etr_a, etr_b, etr_c]
                drawPolygon(color, points)

        if event.type == pygame.MOUSEMOTION and drawing:
            if shape == 6: #eraser
                eraser(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shape+=1 
                shape%=7 

    pygame.display.flip()



# def drawCircleBetween(screen, element1, element2):
#     start, color, mode, width = element1
#     end = element2[0




