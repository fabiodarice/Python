import pygame
pygame.mixer.init()
pygame.init()
print('\033[33mPlayer de MP3\033[m')
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()