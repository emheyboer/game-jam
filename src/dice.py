import random
from sprites import Sprite


class Die:
    def __init__(self, sides: int, sprite: Sprite) -> None:
        self.sides = sides
        self.sprite = sprite
        self.last_roll = 0

    def __str__(self) -> str:
        return f"{self.sides}-sided die"
    
    def __repr__(self) -> str:
        return str(self)
    
    def draw(self, screen, pos: tuple[float, float], size = None):
        self.sprite.draw(screen, pos, size=size, text=str(self.last_roll))

    @staticmethod
    def predefined(sprites, name: str):
        dice = {
            'd20_white': WhiteDie(20, sprites['d20_white']),
            'd12_white': WhiteDie(12, sprites['d12_white']),
            'd10_white': WhiteDie(10, sprites['d10_white']),
            'd8_white': WhiteDie(8, sprites['d8_white']),
            'd6_white': WhiteDie(6, sprites['d6_white']),
            'd4_white': WhiteDie(4, sprites['d4_white']),

            # 'd20_blue_green': WhiteDie(20, sprites['d20_blue_green']),
            # 'd12_blue_green': WhiteDie(12, sprites['d12_blue_green']),
            # 'd10_blue_green': WhiteDie(10, sprites['d10_blue_green']),
            # 'd8_blue_green': WhiteDie(8, sprites['d8_blue_green']),
            # 'd6_blue_green': WhiteDie(6, sprites['d6_blue_green']),
            # 'd4_blue_green': WhiteDie(4, sprites['d4_blue_green']),

            # 'd20_brown_yellow': WhiteDie(20, sprites['d20_brown_yellow']),
            # 'd12_brown_yellow': WhiteDie(12, sprites['d12_brown_yellow']),
            # 'd10_brown_yellow': WhiteDie(10, sprites['d10_brown_yellow']),
            # 'd8_brown_yellow': WhiteDie(8, sprites['d8_brown_yellow']),
            # 'd6_brown_yellow': WhiteDie(6, sprites['d6_brown_yellow']),
            # 'd4_brown_yellow': WhiteDie(4, sprites['d4_brown_yellow']),

            # 'd20_inverted': WhiteDie(20, sprites['d20_inverted']),
            # 'd12_inverted': WhiteDie(12, sprites['d12_inverted']),
            # 'd10_inverted': WhiteDie(10, sprites['d10_inverted']),
            # 'd8_inverted': WhiteDie(8, sprites['d8_inverted']),
            # 'd6_inverted': WhiteDie(6, sprites['d6_inverted']),
            # 'd4_inverted': WhiteDie(4, sprites['d4_inverted']),

            # 'd20_pink_blue': WhiteDie(20, sprites['d20_pink_blue']),
            # 'd12_pink_blue': WhiteDie(12, sprites['d12_pink_blue']),
            # 'd10_pink_blue': WhiteDie(10, sprites['d10_pink_blue']),
            # 'd8_pink_blue': WhiteDie(8, sprites['d8_pink_blue']),
            # 'd6_pink_blue': WhiteDie(6, sprites['d6_pink_blue']),
            # 'd4_pink_blue': WhiteDie(4, sprites['d4_pink_blue']),

            # 'd20_agender': WhiteDie(20, sprites['d20_agender']),
            # 'd12_agender': WhiteDie(12, sprites['d12_agender']),
            # 'd10_agender': WhiteDie(10, sprites['d10_agender']),
            # 'd8_agender': WhiteDie(8, sprites['d8_agender']),
            # 'd6_agender': WhiteDie(6, sprites['d6_agender']),
            # 'd4_agender': WhiteDie(4, sprites['d4_agender']),

            'd20_genderfluid': GenderfliudDie(20, sprites),
            'd12_genderfluid': GenderfliudDie(12, sprites),
            'd10_genderfluid': GenderfliudDie(10, sprites),
            'd8_genderfluid': GenderfliudDie(8, sprites),
            'd6_genderfluid': GenderfliudDie(6, sprites),
            'd4_genderfluid': GenderfliudDie(4, sprites),

            # 'd20_genderqueer': WhiteDie(20, sprites['d20_genderqueer']),
            # 'd12_genderqueer': WhiteDie(12, sprites['d12_genderqueer']),
            # 'd10_genderqueer': WhiteDie(10, sprites['d10_genderqueer']),
            # 'd8_genderqueer': WhiteDie(8, sprites['d8_genderqueer']),
            # 'd6_genderqueer': WhiteDie(6, sprites['d6_genderqueer']),
            # 'd4_genderqueer': WhiteDie(4, sprites['d4_genderqueer']),

            'd20_nonbinary': NonBinaryDie(20, sprites['d20_nonbinary']),
            'd12_nonbinary': NonBinaryDie(12, sprites['d12_nonbinary']),
            'd10_nonbinary': NonBinaryDie(10, sprites['d10_nonbinary']),
            'd8_nonbinary': NonBinaryDie(8, sprites['d8_nonbinary']),
            'd6_nonbinary': NonBinaryDie(6, sprites['d6_nonbinary']),
            'd4_nonbinary': NonBinaryDie(4, sprites['d4_nonbinary']),

            'd20_rainbow': RainbowDie(20, sprites['d20_rainbow']),
            'd12_rainbow': RainbowDie(12, sprites['d12_rainbow']),
            'd10_rainbow': RainbowDie(10, sprites['d10_rainbow']),
            'd8_rainbow': RainbowDie(8, sprites['d8_rainbow']),
            'd6_rainbow': RainbowDie(6, sprites['d6_rainbow']),
            'd4_rainbow': RainbowDie(4, sprites['d4_rainbow']),

            # 'd20_trans': WhiteDie(20, sprites['d20_trans']),
            # 'd12_trans': WhiteDie(12, sprites['d12_trans']),
            # 'd10_trans': WhiteDie(10, sprites['d10_trans']),
            # 'd8_trans': WhiteDie(8, sprites['d8_trans']),
            # 'd6_trans': WhiteDie(6, sprites['d6_trans']),
            # 'd4_trans': WhiteDie(4, sprites['d4_trans']),

            # 'd20_purple_pink': WhiteDie(20, sprites['d20_purple_pink']),
            # 'd12_purple_pink': WhiteDie(12, sprites['d12_purple_pink']),
            # 'd10_purple_pink': WhiteDie(10, sprites['d10_purple_pink']),
            # 'd8_purple_pink': WhiteDie(8, sprites['d8_purple_pink']),
            # 'd6_purple_pink': WhiteDie(6, sprites['d6_purple_pink']),
            # 'd4_purple_pink': WhiteDie(4, sprites['d4_purple_pink']),

            # 'd20_red_yellow': WhiteDie(20, sprites['d20_red_yellow']),
            # 'd12_red_yellow': WhiteDie(12, sprites['d12_red_yellow']),
            # 'd10_red_yellow': WhiteDie(10, sprites['d10_red_yellow']),
            # 'd8_red_yellow': WhiteDie(8, sprites['d8_red_yellow']),
            # 'd6_red_yellow': WhiteDie(6, sprites['d6_red_yellow']),
            # 'd4_red_yellow': WhiteDie(4, sprites['d4_red_yellow']),
        }
        return dice[name]


class WhiteDie(Die):
    def roll(self) -> int:
        value = random.randint(1, self.sides)
        self.last_roll = value
        return value


class GenderfliudDie(Die):
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
    

class NonBinaryDie(Die):
    def roll(self) -> int:
        value = random.randint(3, self.sides)
        self.last_roll = value
        return value
    

class RainbowDie(Die):
    def roll(self) -> int:
        total = 0
        # exploding dice
        while True:
            value = random.randint(1, self.sides)
            total += value

            if value != self.sides:
                self.last_roll = total
                return total