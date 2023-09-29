import pygame

from typing import Any

class charater(pygame.sprite.Sprite):

    def __init__(self, seq, color: tuple[int, int, int]) -> None:
        self.width, self.height = 50 ,50
        self.radius = 10
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.r, self.g, self.b = color
        self.alpha = 255
        self.alpha_change = -20
        self.image.fill((255, 255, 255, 0))
        self.x, self.y = 860, 860
        self.index = 0
        self.seq = seq
        self.animate = False
        self.in_aimate = False
        self.step = 0
        
        pygame.draw.circle(self.image, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius)
        super().__init__()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.animate:
            self.step = kwargs["step"]
            self.animate = False
        if self.step > 0:
            self.do_animate(kwargs["map"])

    def do_animate(self, map):
        if self.step <= 0:
            return
        self.alpha += self.alpha_change
        if self.alpha < 255:
            if self.alpha <= 0:
                self.alpha = 0
                self.alpha_change = -self.alpha_change
                self.move(map)

            self.image.fill((255, 255, 255, 0))
            pygame.draw.circle(self.image, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius)

        else:
            self.alpha = 255
            self.alpha_change = -self.alpha_change
            self.image.fill((255, 255, 255, 0))
            pygame.draw.circle(self.image, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius) 
            self.step -= 1
            return self.do_animate(self.step)

    def move(self, map):
        map[self.index] -= 1
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

        map[self.index] += 1
        
        