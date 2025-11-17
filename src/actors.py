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

        self.atk_index = 0
        self.attacks = attacks

    def roll_attack(self, atk_index: int | None = None) -> tuple[int, list[Die]]:
        """
        Roll the next attack from `attacks`
        """
        self.atk_index = atk_index if atk_index is not None else self.atk_index
        attack = self.attacks[self.atk_index]

        self.atk_index += 1
        if self.atk_index >= len(self.attacks):
            self.atk_index = 0

        return attack.roll_attack(self.dice_bag)
