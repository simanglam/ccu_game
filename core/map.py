import pygame
from core.charater import charater

class map:
    def __init__(self) -> None:
        self.map = pygame.image.load("map2.png")
        self.old_map = self.map.copy()

        self.width, self.height = self.map.get_size()
        self.chunk = {}

        self.current_team = 0
        self.animate = False

        self.player = pygame.sprite.Group()
        team1 = charater(0, (0, 0, 255))
        team2 = charater(1, (255, 0, 0))
        team3 = charater(2, (0, 255, 0))

        self.player.add(team1)
        self.player.add(team2)
        self.player.add(team3)

        for i in range(0, 28):
            self.chunk[i] = 0
        self.chunk[0] = 3


    def move(self, index, state):
        if state:
            self.chunk[index] += 1
        else:
            self.chunk[index] -= 1

    def collision(self, index: int) -> int:
        if self.chunk[index] == 0:
            return None
        else:
            return self.chunk[index]

    def get_current_team(self) -> charater:
        return self.player.sprites()[self.current_team]
    
    def change_current_team(self, new_team_index: int):
        self.current_team = new_team_index

    def update(self, step = 0):
        self.map.blit(self.old_map, (0, 0))
        self.player.update(step = 0, map = self.chunk)

        for i in self.player.sprites():
            if self.chunk[i.index] > 1:
                self.map.blit(i.image, (i.x + 20 * i.seq - 1, i.y))
            else:
                self.map.blit(i.image, (i.x, i.y))

        if step > 0:
            self.player.sprites()[self.current_team].animate = True
            self.player.sprites()[self.current_team].update(step = step, map = self.chunk)
            
            self.current_team += 1
            if self.current_team >= 3:
                self.current_team = 0