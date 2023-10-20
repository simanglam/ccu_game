import pygame
import random

class panel:

    def __init__(self, map):
        self.width, self.height = 200, 200
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((209, 130, 81))
        self.map = map
        self.times = -1
        self.target = 0
        self.image_array = []
        for i in range(1, 7):
            self.image_array.append(pygame.image.load(f"Dice/dice-{i}.png"))

        self.font = pygame.font.Font("Times New Roman.ttf", 60)

    def render(self, target):
        self.image.fill((255, 255, 255))
        self.image.blit(self.image_array[target - 1], (0, 0))

        self.times -= 1

    def roll(self):
        self.times = 60