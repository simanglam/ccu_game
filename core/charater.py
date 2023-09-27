import pygame

from typing import Any

class charater(pygame.sprite.Sprite):

    def __init__(self, seq, color) -> None:
        self.width, self.height = 50 ,50
        self.radius = 10
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.color = color
        self.image.fill((255, 255, 255, 0))
        self.x, self.y = 1000, 1000
        self.index = 0
        self.seq = seq
        
        pygame.draw.circle(self.image, color, (self.width / 2, self.height / 2), self.radius)
        super().__init__()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if kwargs["step"] != 0:
            self.move(kwargs["step"])

    def move(self, step = 0):
        if step == 0:
            return
        if self.index <= 4:
            self.y -= 100

        elif self.index <= 9:
            self.x -= 100
    
        elif self.index <= 14:
            self.y += 100

        elif self.index <= 19:
            self.x += 100

        self.index += 1

        if self.index > 19:
            self.index = 0

        return self.move(step - 1)