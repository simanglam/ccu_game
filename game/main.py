from typing import Any
import pygame
import asyncio


from core import game

pygame.init()

main_game = game()

asyncio.run(main_game.run())
