from diceBag import DiceBag
from dice import Die, UnionDie, FireDie, PoisonDie, MoneyDie
from sprites import Sprite

class Attack:
    def __init__(self, sets: list[tuple[int, int]], gambling: bool = False) -> None:
        # list of tuples e.g. (3, 5) representing dice to roll e.g. 3d5
        self.sets = sets
        self.gambling = gambling

    def pull_from_bag(self, dice_bag: DiceBag) -> list[Die]:
        if self.gambling:
            return self.gamble(dice_bag)
        
        dice = []
        for n_dice, n_sides in self.sets:
            pulled = dice_bag.pull_dice(n_dice, n_sides)
            dice.extend(pulled)
        return dice
    
    def gamble(self, dice_bag: DiceBag) -> list[Die]:
        dice = dice_bag.pull_any_dice(1)
        if len(dice) != 1:
            return []
        [die] = dice

        n_dice = die.roll()
        dice_bag.add_dice([die])
        print(f"rolled a d{die.sides}, pulling {n_dice} dice")

        dice = dice_bag.pull_any_dice(n_dice)
        return dice
    
    def roll_attack(self, dice_bag: DiceBag) -> tuple[int, bool, bool, int, list[Die]]:
        dice = self.pull_from_bag(dice_bag)

        total = 0
        union = []
        fire = False
        poison = False
        money = 0
        for die in dice:
            if type(die) == UnionDie:
                union.append(die)
            elif type(die) == FireDie:
                fire = True
            elif type(die) == PoisonDie:
                poison = True
            elif type(die) == MoneyDie:
                money += 1
            total += die.roll()
        
        for die in union:
            die.last_roll += len(union)

        return (total + len(union)**2, fire, poison, money, dice)
    
    def is_possible(self, dice_bag: DiceBag) -> bool:
        dice = self.pull_from_bag(dice_bag)
        count = len(dice)
        dice_bag.add_dice(dice)
        return count > 0
    
    def __str__(self) -> str:
        if self.gambling:
            return "???"
        
        set_strs = []
        for n_dice, n_sides in self.sets:
            set_strs.append(f"{n_dice}d{n_sides}")
        return '+'.join(set_strs)

    def __repr__(self) -> str:
        return str(self)