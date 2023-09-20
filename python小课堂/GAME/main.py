import pygame
from pygame.locals import *
import random

pygame.init()
DISPLAYER = pygame.display.set_mode((800,600))


while True:
    for event in pygame.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update

