import random
from sprites import Sprite
from dice import Die

class DiceBag:
    def __init__(self, dice: list[Die], sprite: Sprite):
        self.contents = {n: [] for n in [4, 6, 8, 10, 12, 20]}
        self.add_dice(dice)

        self.sprite = sprite

    def add_dice(self, dice):
        for die in dice:
            num_sides = len(die.sides)
            self.contents[num_sides].append(die)

    def pull_dice(self, n_dice: int, n_sides: int) -> list[Die]:
        dice = []
        options = self.contents[n_sides]
        for i in range(n_dice):
            if len(options) == 0:
                break

            die = random.choice(options)
            options.remove(die)
            dice.append(die)

        return dice
    
    def all_dice(self) -> list[Die]:
        dice = []
        for n_sided_dice in self.contents.values():
            dice.extend(n_sided_dice)
        return dice
    
    def size(self) -> int:
        return len(self.all_dice())
    
    def __str__(self) -> str:
        return f"dice bag containing: {self.all_dice()}"

    def __repr__(self) -> str:
        return str(self)
        
    def draw(self, screen, pos: tuple[float, float], scale = None):
        self.sprite.draw(screen, pos, scale=scale)