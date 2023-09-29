from typing import Any
import pygame

from pygame import Rect, draw
from pygame.locals import *

from core import game

pygame.init()

main_game = game()

main_game.run()

pygame.quit()