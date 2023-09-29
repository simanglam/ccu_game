import pygame
from .charater import charater

class monitor:
    
    def __init__(self):
        self.screen = pygame.surface.Surface((400, 100))
        self.screen.fill((255,255,255))
        self.width, self.height = self.screen.get_size()
        self.font = pygame.font.Font(pygame.font.match_font("haranoajigothictw"))

    def info(self, players: list) -> str:
        result = ""

        for i in players.sprites():
            result += f"隊伍{i.seq} 位置{i.index}"
        
        return result

    def update(self, charater: pygame.sprite.Group):
        self.screen.fill((255,255,255))
        self.screen.blit(self.font.render(f"{self.info(charater)}", 1, (0, 0, 0)), (0, 0))

