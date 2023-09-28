import pygame

from typing import Any

class charater(pygame.sprite.Sprite):

    def __init__(self, seq, color: pygame.color.Color) -> None:
        self.width, self.height = 50 ,50
        self.radius = 10
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.color = color
        self.image.fill(self.color)
        self.x, self.y = 860, 860
        self.index = 0
        self.seq = seq
        
        pygame.draw.circle(self.image, (255, 255), (self.width / 2, self.height / 2), self.radius)
        super().__init__()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if kwargs["step"] != 0:
            self.move(kwargs["step"])

    def move(self, step = 0):
        if step == 0:
            return
        if self.index <= 6:
            self.y -= 100

        elif self.index <= 13:
            self.x -= 100
    
        elif self.index <= 20:
            self.y += 100

        elif self.index <= 27:
            self.x += 100

        self.index += 1

        if self.index > 27:
            self.index = 0

        return self.move(step - 1)