import random
from sprites import Sprite

class Die:
    def __init__(self, sides: list[int] | range, sprite: Sprite):
        self.sides = sides
        self.sprite = sprite

        self.last_roll = 0

    def roll(self) -> int:
        value = random.choice(self.sides)
        self.last_roll = value
        return value
    
    def __str__(self) -> str:
        return f"{len(self.sides)}-sided die"
    
    def __repr__(self) -> str:
        return str(self)
    
    def draw(self, screen, pos: tuple[float, float], size = None):
        self.sprite.draw(screen, pos, size=size, text=str(self.last_roll))