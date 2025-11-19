from sprites import Sprite
from diceBag import DiceBag
from dice import Die
from attack import Attack

class Actor:
    def __init__(self, name: str, profile_art: Sprite, dice_box_art: Sprite, dice_bag: DiceBag, attacks: list[Attack]):
        self.name = name
        self.profile_art = profile_art
        self.dice_box_art = dice_box_art
        self.dice_bag = dice_bag

        self.atk_index = -1
        self.attacks = attacks
        self.fireStreak = 0

    def next_attack(self) -> int | None:
        index = self.atk_index % len(self.attacks)
        while True:
            index = (index + 1) % len(self.attacks)
            if self.attacks[index].is_possible(self.dice_bag):
                return index
            if index == self.atk_index:
                return None

    def roll_attack(self, atk_index: int | None = None) -> tuple[int, list[Die]]:
        """
        Roll the next attack from `attacks`
        """
        if atk_index is not None:
            self.atk_index = atk_index
        else:
            next = self.next_attack()
            if next is None:
                return (0, [])
            self.atk_index = next
        
        atk = self.attacks[self.atk_index]

        total, fire, dice = atk.roll_attack(self.dice_bag)

        if fire:
            self.fireStreak += 1
            total += self.fireStreak
        else:
            self.fireStreak = 0

        return total, dice
