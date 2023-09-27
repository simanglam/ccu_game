from typing import Any
import pygame

from pygame import Rect, draw
from pygame.locals import *

from core.map import map

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
width, height = screen.get_size()
print(width, height)

bg = pygame.Surface(screen.get_size())
bg.fill((255,255,255))


game_map = map()

running = True

while running:
        screen.blit(bg, (0, 0))
        game_map.update()
        screen.blit(game_map.map, ((width - game_map.width) / 2, (height - game_map.height) / 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_map.update(step = 1)
                if event.key == pygame.K_2:
                    game_map.update(step = 2)
                if event.key == pygame.K_3:
                    game_map.update(step = 3)
                if event.key == pygame.K_4:
                    game_map.update(step = 4)
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(30)

pygame.quit()