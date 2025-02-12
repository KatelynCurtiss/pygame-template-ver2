# Katelyn Curtiss
# Febraury 11 2025
# Pygame Template 

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60 # Frames per second

PURPLE = (128, 0, 128)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Template")

clock = pygame.time.Clock() 

running = True
while running:

   for event in pygame.event.get():
    if event.type == pygame.QUIT: 

      running = False

screen.fill(PURPLE) 
pygame.display.flip() 


clock.tick(FPS)

pygame.quit()
sys.exit()