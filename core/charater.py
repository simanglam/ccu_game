import pygame

from typing import Any

class charater(pygame.sprite.Sprite):

    def __init__(self, seq, color: tuple[int, int, int]) -> None:
        super().__init__()
        self.width, self.height = 50 ,50
        self.radius = 10
        self.screen = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.screen = self.screen.convert_alpha()
        self.r, self.g, self.b = color
        self.alpha = 255
        self.alpha_change = -20
        self.screen.fill((255, 255, 255, 0))
        self.x, self.y = 860, 860
        self.index = 0
        self.seq = seq
        self.step: int = 0
        
        pygame.draw.circle(self.screen, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius)

    def set_step(self, step: int) -> None:
        self.step = step

    def update(self, *args: Any, **kwargs: Any) -> None:
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

            self.screen.fill((255, 255, 255, 0))
            pygame.draw.circle(self.screen, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius)

        else:
            self.alpha = 255
            self.alpha_change = -self.alpha_change
            self.screen.fill((255, 255, 255, 0))
            pygame.draw.circle(self.screen, (self.r, self.g, self.b, self.alpha), (self.width / 2, self.height / 2), self.radius) 
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
        
        