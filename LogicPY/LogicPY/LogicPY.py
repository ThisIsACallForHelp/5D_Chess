
import pygame.display
import pygame.event
import pygame.event
import pygame

pygame.init()

screen = pygame.display.set_mode((1040,640))

Run = True

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

pygame.quit()