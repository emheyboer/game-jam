from diceBag import DiceBag
from dice import Die

class Attack:
    def __init__(self, sets: list[tuple[int, int]]) -> None:
        # list of tuples e.g. (3, 5) representing dice to roll e.g. 3d5
        self.sets = sets

    def pull_from_bag(self, dice_bag: DiceBag) -> list[Die]:
        dice = []
        for n_dice, n_sides in self.sets:
            pulled = dice_bag.pull_dice(n_dice, n_sides)
            dice.extend(pulled)
        return dice
    
    def roll_attack(self, dice_bag: DiceBag) -> tuple[int, list[Die]]:
        dice = self.pull_from_bag(dice_bag)

        total = 0
        for die in dice:
            total += die.roll()
        
        return (total, dice)