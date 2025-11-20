import random
from sprites import Sprite
from dice import Die, GlassDie

class DiceBag:
    def __init__(self, dice: list[Die], sprite: Sprite):
        self.contents = {n: [] for n in [4, 6, 8, 10, 12, 20]}
        self.add_dice(dice)

        self.sprite = sprite

    def add_dice(self, dice: list[Die]):
        for die in dice:
            if type(die) == GlassDie and die.broken:
                continue
            self.contents[die.sides].append(die)

    def pull_dice(self, n_dice: int, n_sides: int) -> list[Die]:
        """
        Pull x n-sided dice from the bag. Dice must be re-added later as needed
        """
        dice = []
        options = self.contents[n_sides]
        for i in range(n_dice):
            if len(options) == 0:
                break

            die = random.choice(options)
            options.remove(die)
            dice.append(die)

        return dice
    
    def pull_any_dice(self, n_dice: int) -> list[Die]:
        all_dice = self.all_dice()
        n_dice = min(n_dice, len(all_dice))
        dice = random.sample(all_dice, n_dice)
        
        for die in dice:
            self.contents[die.sides].remove(die)

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
        
    def draw(self, screen, pos: tuple[float, float], size = None):
        self.sprite.draw(screen, pos, size=size)