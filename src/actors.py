from sprites import Sprite
from diceBag import DiceBag
from dice import Die
from attack import Attack

class Actor:
    def __init__(self, name: str, profile_art: Sprite, dice_box_art: Sprite, dice_bag: DiceBag, attack: Attack):
        self.name = name
        self.profile_art = profile_art
        self.dice_box_art = dice_box_art
        self.dice_bag = dice_bag
        self.attack = attack

    def roll_attack(self) -> tuple[int, list[Die]]:
        return self.attack.roll_attack(self.dice_bag)
