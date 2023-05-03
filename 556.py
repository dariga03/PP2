import pygame
import os 

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Music Player')

music_folder = r'C:\dori\pp2\lab7\songs'
music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]

i = 0
pygame.mixer.music.load(music_files[i]) 
pygame.mixer.music.play()

prev_button = pygame.draw.polygon(screen, (80, 208, 255), ((30, 425), (80, 400),(80, 450))) #triangle blue
play_button = pygame.draw.rect(screen, (255, 255, 0), (130, 400, 50, 50)) #yellow rectangle
pause_button = pygame.draw.circle(screen, (0, 255, 0), (255, 425), 25) #green circle
stop_button = pygame.draw.rect(screen, (255, 0, 0), (330, 400, 50, 50)) #red rectangle
next_button = pygame.draw.polygon(screen, (80, 208, 255), ((480, 425), (430, 400),(430, 450)))  #blue triangle

num_of_songs = len(os.listdir(r'C:\dori\pp2\lab7\songs'))


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if pause_button.collidepoint(event.pos): 
                pygame.mixer.music.pause() 
            elif play_button.collidepoint(event.pos): 
                pygame.mixer.music.unpause()
            elif stop_button.collidepoint(event.pos): 
                pygame.mixer.music.stop()
            elif next_button.collidepoint(event.pos):
                while i < num_of_songs:
                    pygame.mixer.music.load(music_files[i+1]) 
                    pygame.mixer.music.play()
                    i += 1
                    break
            elif prev_button.collidepoint(event.pos):
                while i > 0:
                    pygame.mixer.music.load(music_files[i-1]) 
                    pygame.mixer.music.play()
                    i -= 1
                    break
                   
                
    pygame.display.update()