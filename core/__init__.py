import pygame
import asyncio

from .map import map
from .monitor import monitor
from pygame.locals import *

class game:

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
        self.width, self.height = self.screen.get_size()

        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255,255,255))

        self.game_map = map()

        self.monitor = monitor()

        self.running = True

    def reload(self):
        del self.game_map
        del self.monitor
        self.game_map = map()
        self.monitor = monitor()

    async def run(self):
        while self.running:
            self.screen.blit(self.bg, (0, 0))
            self.game_map.update()
            self.monitor.update(self.game_map.get_players())
            self.screen.blit(self.game_map.map, ((self.width - self.game_map.width) / 2, (self.height - self.game_map.height) / 2))
            self.screen.blit(self.monitor.screen, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                
                if event.type == pygame.KEYDOWN:
                    if event.mod & pygame.KMOD_SHIFT:
                        if event.key == pygame.K_0:
                            self.game_map.change_current_team(0)
                        if event.key == pygame.K_1:
                            self.game_map.change_current_team(1)
                        if event.key == pygame.K_2:
                            self.game_map.change_current_team(2)
                        if event.key == pygame.K_3:
                            self.game_map.change_current_team(3)
                        if event.key == pygame.K_4:
                            self.game_map.change_current_team(4)
                    else:
                        if event.key == pygame.K_1:
                            self.game_map.update(step = 1)
                        if event.key == pygame.K_2:
                            self.game_map.update(step = 2)
                        if event.key == pygame.K_3:
                            self.game_map.update(step = 3)
                        if event.key == pygame.K_4:
                            self.game_map.update(step = 4)
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                        if event.key == pygame.K_r:
                            self.reload()


            pygame.display.update()
            await asyncio.sleep(0)