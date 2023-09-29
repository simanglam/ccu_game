import pygame
from .charater import charater

class monitor:
    
    def __init__(self):
        self.screen = pygame.surface.Surface((100, 100))
        self.screen.fill((255,255,255))
        self.width, self.height = self.screen.get_size()
        self.font = pygame.font.Font(pygame.font.match_font("haranoajigothictw"))

    def update(self, charater: charater):
        self.screen.fill((255,255,255))
        self.screen.blit(self.font.render(f"隊伍 {charater.seq}", 1, (0, 0, 0)), (0, 0))
