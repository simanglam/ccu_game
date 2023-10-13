import pygame
from .charater import charater

class monitor:
    
    def __init__(self):
        self.screen = pygame.surface.Surface((400, 500))
        self.screen.fill((255,255,255))
        self.width, self.height = self.screen.get_size()
        self.image_array = [pygame.image.load("./charater_image/ch1.png"), pygame.image.load("./charater_image/ch2.png"), pygame.image.load("./charater_image/ch3.png")]
        self.image_array = [pygame.transform.scale(i, (400, 400)) for i in self.image_array]
        self.font = pygame.font.Font("Times New Roman.ttf", 60)
        self.text = self.font.render("Current Team", 1, (0, 0, 0))
        self.text_rect = self.text.get_rect(center = (200, 450))

    def info(self, players: list) -> str:
        result = ""

        for i in players.sprites():
            result += f"隊伍{i.seq} 位置{i.index}"
        
        return result

    def update(self, current_index: int):
        self.screen.fill((255,255,255))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.image_array[current_index], (0, 0))

