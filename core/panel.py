import pygame
import random

class panel:

    def __init__(self, map):
        self.width, self.height = 640, 640
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((209, 130, 81))
        self.map = map
        self.times = -1
        self.target = 0

        self.font = pygame.font.Font("Times New Roman.ttf", 60)

    def render(self, target):
        self.image.fill((255, 255, 255))
        self.image.blit(self.font.render(str(target), 1, (0, 0, 0)), (250, 250))

        self.times -= 1

        

    def roll(self):
        self.times = random.randint(120, 180)