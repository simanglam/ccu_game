import pygame
from .charater import charater
from .panel import panel

class map:
    def __init__(self) -> None:
        self.map = pygame.image.load("map.png")
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

        self.panel = panel()


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

    def get_current_team(self) -> int:
        return self.current_team
    
    def get_players(self) -> pygame.sprite.Group:
        return self.player
    
    def change_current_team(self, new_team_index: int):
        self.current_team = new_team_index

    def update(self, step = 0):
        self.render()

        if step > 0:
            self.player.sprites()[self.current_team].move(step)
            self.current_team += 1
            if self.current_team >= 3:
                self.current_team = 0

    def render(self):
        self.map.blit(self.old_map, (0, 0))
        #self.panel.render(self.current_team)
        #self.map.blit(self.panel.image, (220, 220))

        for i in range(0, len(self.player.sprites())):
            self.player.sprites()[i].update(map = self.chunk, current = True if i == self.current_team else None)
            shift = 0
            for x in range(i, len(self.player.sprites())):
                if self.player.sprites()[i] != self.player.sprites()[x]:
                    if self.player.sprites()[i].index == self.player.sprites()[x].index:
                        if self.player.sprites()[i].seq < self.player.sprites()[x].seq:
                            shift += 1
            self.map.blit(self.player.sprites()[i].screen, self.player.sprites()[i].cal_coordinate(shift))