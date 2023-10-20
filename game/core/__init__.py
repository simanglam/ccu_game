import pygame
import asyncio, random

from .panel import panel
from .map import map
from .monitor import monitor
from .web_server import ControllServer
from pygame.locals import *

class game:

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1920, 1080))
        self.width, self.height = self.screen.get_size()

        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255,255,255))

        self.panel = panel(self)
        self.animate = False

        self.game_map = map()

        self.monitor = monitor()
        self.controller = ControllServer()

        self.running = True
        self.stop = False

    def reload(self):
        del self.game_map
        del self.monitor
        self.game_map = map()
        self.monitor = monitor()

    async def run(self):
        while self.running:
            keys = pygame.key.get_pressed()
            self.screen.blit(self.bg, (0, 0))
            self.game_map.render()
            self.monitor.update(self.game_map.get_current_team())
            self.controller.update()
            self.screen.blit(self.game_map.map, ((self.width - self.game_map.width) / 2, (self.height - self.game_map.height) / 2))
            if self.animate:
                target = random.randint(1, 6)
                self.panel.render(target)
                pygame.time.delay(int(200 * (60 - self.panel.times) / 60))
                self.screen.blit(self.panel.image, ((self.width - self.game_map.width) / 2 + 220, (self.height - self.game_map.height) / 2 + 220))
            self.screen.blit(self.monitor.screen, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                            self.running = False
                        
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if keys[pygame.key.key_code('w')]:
                        self.panel.roll()
                        self.animate = True

            if self.controller.is_trigger():
                self.panel.roll()
                self.animate = True
                print(self.controller.server.trigger)
                self.controller.server.trigger = False

            pygame.display.update()
            if self.panel.times == 1:
                self.animate = False
                self.game_map.update(target)
                pygame.time.delay(1000)
                self.stop = False
                self.panel.times -= 1


            self.clock.tick(30)
            await asyncio.sleep(0)