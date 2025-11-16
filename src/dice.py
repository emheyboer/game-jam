import random
import pygame
from sprites import Sprite

class Die:
    def __init__(self, sides: list[int], sprite: Sprite, textOffset: tuple[int, int]):
        self.sides = sides
        self.sprite = sprite
        self.offsetX, self.offsetY = textOffset
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

        self.last_roll = 0

    def roll(self) -> int:
        value = random.choice(self.sides)
        self.last_roll = value
        return value
    
    def __str__(self) -> str:
        return f"{len(self.sides)}-sided die"
    
    def __repr__(self) -> str:
        return str(self)
    
    def draw(self, screen, x: float, y: float, scale = None):
        self.sprite.draw(screen, x, y, scale=scale)

        text = self.font.render(str(self.last_roll), False, (0, 0, 0))

        x = x + self.offsetX
        y = y + self.offsetY

        screen.blit(text, (x, y))