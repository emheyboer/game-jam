import random
from sprites import Sprite


class Die:
    def __init__(self, sides: int, sprite: Sprite) -> None:
        self.sides = sides
        self.sprite = sprite
        self.last_roll = 0

    def __str__(self) -> str:
        return f"{self.sides}-sided {type(self).__name__}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def draw(self, screen, pos: tuple[float, float], size = None):
        self.sprite.draw(screen, pos, size=size, text=str(self.last_roll))

    def roll(self) -> int:
        value = random.randint(1, self.sides)
        self.last_roll = value
        return value

    @staticmethod
    def predefined(sprites, name: str):
        dice = {
            'd20_basic': BasicDie(20, sprites['d20_white']),
            'd12_basic': BasicDie(12, sprites['d12_white']),
            'd10_basic': BasicDie(10, sprites['d10_white']),
            'd8_basic': BasicDie(8, sprites['d8_white']),
            'd6_basic': BasicDie(6, sprites['d6_white']),
            'd4_basic': BasicDie(4, sprites['d4_white']),

            'd20_glass': GlassDie(20, sprites['d20_blue_green']),
            'd12_glass': GlassDie(12, sprites['d12_blue_green']),
            'd10_glass': GlassDie(10, sprites['d10_blue_green']),
            'd8_glass': GlassDie(8, sprites['d8_blue_green']),
            'd6_glass': GlassDie(6, sprites['d6_blue_green']),
            'd4_glass': GlassDie(4, sprites['d4_blue_green']),

            'd20_stone': StoneDie(20, sprites['d20_brown_yellow']),
            'd12_stone': StoneDie(12, sprites['d12_brown_yellow']),
            'd10_stone': StoneDie(10, sprites['d10_brown_yellow']),
            'd8_stone': StoneDie(8, sprites['d8_brown_yellow']),
            'd6_stone': StoneDie(6, sprites['d6_brown_yellow']),
            'd4_stone': StoneDie(4, sprites['d4_brown_yellow']),

            'd20_union': UnionDie(20, sprites['d20_inverted']),
            'd12_union': UnionDie(12, sprites['d12_inverted']),
            'd10_union': UnionDie(10, sprites['d10_inverted']),
            'd8_union': UnionDie(8, sprites['d8_inverted']),
            'd6_union': UnionDie(6, sprites['d6_inverted']),
            'd4_union': UnionDie(4, sprites['d4_inverted']),

            'd20_advantage': AdvantageDie(20, sprites['d20_pink_blue']),
            'd12_advantage': AdvantageDie(12, sprites['d12_pink_blue']),
            'd10_advantage': AdvantageDie(10, sprites['d10_pink_blue']),
            'd8_advantage': AdvantageDie(8, sprites['d8_pink_blue']),
            'd6_advantage': AdvantageDie(6, sprites['d6_pink_blue']),
            'd4_advantage': AdvantageDie(4, sprites['d4_pink_blue']),

            'd20_poison': PoisonDie(20, sprites['d20_agender']),
            'd12_poison': PoisonDie(12, sprites['d12_agender']),
            'd10_poison': PoisonDie(10, sprites['d10_agender']),
            'd8_poison': PoisonDie(8, sprites['d8_agender']),
            'd6_poison': PoisonDie(6, sprites['d6_agender']),
            'd4_poison': PoisonDie(4, sprites['d4_agender']),

            'd20_fluid': FluidDie(20, sprites),
            'd12_fluid': FluidDie(12, sprites),
            'd10_fluid': FluidDie(10, sprites),
            'd8_fluid': FluidDie(8, sprites),
            'd6_fluid': FluidDie(6, sprites),
            'd4_fluid': FluidDie(4, sprites),

            'd20_money': MoneyDie(20, sprites['d20_genderqueer']),
            'd12_money': MoneyDie(12, sprites['d12_genderqueer']),
            'd10_money': MoneyDie(10, sprites['d10_genderqueer']),
            'd8_money': MoneyDie(8, sprites['d8_genderqueer']),
            'd6_money': MoneyDie(6, sprites['d6_genderqueer']),
            'd4_money': MoneyDie(4, sprites['d4_genderqueer']),

            'd20_lucky': LuckyDie(20, sprites['d20_nonbinary']),
            'd12_lucky': LuckyDie(12, sprites['d12_nonbinary']),
            'd10_lucky': LuckyDie(10, sprites['d10_nonbinary']),
            'd8_lucky': LuckyDie(8, sprites['d8_nonbinary']),
            'd6_lucky': LuckyDie(6, sprites['d6_nonbinary']),
            'd4_lucky': LuckyDie(4, sprites['d4_nonbinary']),

            'd20_exploding': ExplodingDie(20, sprites['d20_rainbow']),
            'd12_exploding': ExplodingDie(12, sprites['d12_rainbow']),
            'd10_exploding': ExplodingDie(10, sprites['d10_rainbow']),
            'd8_exploding': ExplodingDie(8, sprites['d8_rainbow']),
            'd6_exploding': ExplodingDie(6, sprites['d6_rainbow']),
            'd4_exploding': ExplodingDie(4, sprites['d4_rainbow']),

            'd20_trans': TransDie(20, sprites['d20_trans']),
            'd12_trans': TransDie(12, sprites['d12_trans']),
            'd10_trans': TransDie(10, sprites['d10_trans']),
            'd8_trans': TransDie(8, sprites['d8_trans']),
            'd6_trans': TransDie(6, sprites['d6_trans']),
            'd4_trans': TransDie(4, sprites['d4_trans']),

            'd20_outlier': OutlierDie(20, sprites['d20_purple_pink']),
            'd12_outlier': OutlierDie(12, sprites['d12_purple_pink']),
            'd10_outlier': OutlierDie(10, sprites['d10_purple_pink']),
            'd8_outlier': OutlierDie(8, sprites['d8_purple_pink']),
            'd6_outlier': OutlierDie(6, sprites['d6_purple_pink']),
            'd4_outlier': OutlierDie(4, sprites['d4_purple_pink']),

            'd20_fire': FireDie(20, sprites['d20_red_yellow']),
            'd12_fire': FireDie(12, sprites['d12_red_yellow']),
            'd10_fire': FireDie(10, sprites['d10_red_yellow']),
            'd8_fire': FireDie(8, sprites['d8_red_yellow']),
            'd6_fire': FireDie(6, sprites['d6_red_yellow']),
            'd4_fire': FireDie(4, sprites['d4_red_yellow']),
        }
        return dice[name]


class BasicDie(Die):
    pass


class FluidDie(Die):
    def __init__(self, sides: int, sprites: dict[str, Sprite]):
        self.sprites = sprites 
        super().__init__(sides, self.get_sprite(sides))

    def roll(self) -> int:
        sides = random.choice([4, 6, 8, 10, 12, 20])
        self.sprite = self.get_sprite(sides)

        value = random.randint(1, sides)
        self.last_roll = value
        return value

    def get_sprite(self, sides: int) -> Sprite:
        return self.sprites[f"d{sides}_genderfluid"]
    

class LuckyDie(Die):
    def roll(self) -> int:
        value = random.randint(3, self.sides)
        self.last_roll = value
        return value
    

class ExplodingDie(Die):
    def roll(self) -> int:
        total = 0
        # exploding dice
        while True:
            value = random.randint(1, self.sides)
            total += value

            if value != self.sides:
                self.last_roll = total
                return total


class GlassDie(Die):
    def __init__(self, sides: int, sprite: Sprite) -> None:
        self.broken = False # DiceBag checks this before re-adding adding
        super().__init__(sides, sprite)

    def roll(self) -> int:
        breaks = random.randint(1,2)
        if breaks == 1:
            self.broken = True

        # only roll the upper half
        value = random.randint(self.sides // 2, self.sides)
        self.last_roll = value
        return value
    

class UnionDie(Die):
    pass


class AdvantageDie(Die):
    def roll(self) -> int:
        a = random.randint(1, self.sides)
        b = random.randint(1, self.sides)
        value = max(a, b)
        self.last_roll = value
        return value
    

class StoneDie(Die):
    def roll(self) -> int:
        value = self.sides // 2
        self.last_roll = value
        return value
    

class FireDie(Die):
    pass


class PoisonDie(Die):
    pass


class OutlierDie(Die):
    def roll(self) -> int:
        avg = (self.sides +1) / 2
        value = random.randint(1, self.sides)
        if value > avg:
            value += avg / 2
        elif value < avg:
            value -= avg / 2
        value = round(value)

        self.last_roll = value
        return value
    

class MoneyDie(Die):
    pass


class TransDie(Die):
    def roll(self) -> int:
        value = random.randint(1, self.sides)
        value *= 1.5
        value = round(value)
        self.last_roll = value
        return value