from sprites import Sprite
from diceBag import DiceBag

class Actor:
    def __init__(self, name: str, profile_art: Sprite, dice_box_art: Sprite, dice_bag: DiceBag):
        self.name = name
        self.profile_art = profile_art
        self.dice_box_art = dice_box_art
        self.dice_bag = dice_bag
