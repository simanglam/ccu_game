import pygame

class panel:

    def __init__(self):
        self.width, self.height = 640, 640
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((209, 130, 81))

        self.image_array = [pygame.image.load("./charater_image/ch1.png"), pygame.image.load("./charater_image/ch2.png"), pygame.image.load("./charater_image/ch3.png")]

    def render(self, seq):
        self.image.fill((209, 130, 81, 255))
        self.image.blit(self.image_array[seq], (0,0))