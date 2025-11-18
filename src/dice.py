import random
from sprites import Sprite

class Die:
    def __init__(self, sides: list[int] | range, sprite: Sprite):
        self.sides = sides
        self.sprite = sprite

        self.last_roll = 0

    def roll(self) -> int:
        value = random.choice(self.sides)
        self.last_roll = value
        return value
    
    def __str__(self) -> str:
        return f"{len(self.sides)}-sided die"
    
    def __repr__(self) -> str:
        return str(self)
    
    def draw(self, screen, pos: tuple[float, float], size = None):
        self.sprite.draw(screen, pos, size=size, text=str(self.last_roll))

    @staticmethod
    def predefined(sprites, name: str):
        dice = {
            'd20_white': Die(range(1,21), sprites['d20_white']),
            'd12_white': Die(range(1,13), sprites['d12_white']),
            'd10_white': Die(range(1,11), sprites['d10_white']),
            'd8_white': Die(range(1,9), sprites['d8_white']),
            'd6_white': Die(range(1,7), sprites['d6_white']),
            'd4_white': Die(range(1,5), sprites['d4_white']),

            'd20_blue_green': Die(range(1,21), sprites['d20_blue_green']),
            'd12_blue_green': Die(range(1,13), sprites['d12_blue_green']),
            'd10_blue_green': Die(range(1,11), sprites['d10_blue_green']),
            'd8_blue_green': Die(range(1,9), sprites['d8_blue_green']),
            'd6_blue_green': Die(range(1,7), sprites['d6_blue_green']),
            'd4_blue_green': Die(range(1,5), sprites['d4_blue_green']),

            'd20_brown_yellow': Die(range(1,21), sprites['d20_brown_yellow']),
            'd12_brown_yellow': Die(range(1,13), sprites['d12_brown_yellow']),
            'd10_brown_yellow': Die(range(1,11), sprites['d10_brown_yellow']),
            'd8_brown_yellow': Die(range(1,9), sprites['d8_brown_yellow']),
            'd6_brown_yellow': Die(range(1,7), sprites['d6_brown_yellow']),
            'd4_brown_yellow': Die(range(1,5), sprites['d4_brown_yellow']),

            'd20_inverted': Die(range(1,21), sprites['d20_inverted']),
            'd12_inverted': Die(range(1,13), sprites['d12_inverted']),
            'd10_inverted': Die(range(1,11), sprites['d10_inverted']),
            'd8_inverted': Die(range(1,9), sprites['d8_inverted']),
            'd6_inverted': Die(range(1,7), sprites['d6_inverted']),
            'd4_inverted': Die(range(1,5), sprites['d4_inverted']),

            'd20_pink_blue': Die(range(1,21), sprites['d20_pink_blue']),
            'd12_pink_blue': Die(range(1,13), sprites['d12_pink_blue']),
            'd10_pink_blue': Die(range(1,11), sprites['d10_pink_blue']),
            'd8_pink_blue': Die(range(1,9), sprites['d8_pink_blue']),
            'd6_pink_blue': Die(range(1,7), sprites['d6_pink_blue']),
            'd4_pink_blue': Die(range(1,5), sprites['d4_pink_blue']),

            'd20_agender': Die(range(1,21), sprites['d20_agender']),
            'd12_agender': Die(range(1,13), sprites['d12_agender']),
            'd10_agender': Die(range(1,11), sprites['d10_agender']),
            'd8_agender': Die(range(1,9), sprites['d8_agender']),
            'd6_agender': Die(range(1,7), sprites['d6_agender']),
            'd4_agender': Die(range(1,5), sprites['d4_agender']),

            'd20_genderfluid': GenderfliudDie(20, sprites),
            'd12_genderfluid': GenderfliudDie(12, sprites),
            'd10_genderfluid': GenderfliudDie(10, sprites),
            'd8_genderfluid': GenderfliudDie(8, sprites),
            'd6_genderfluid': GenderfliudDie(6, sprites),
            'd4_genderfluid': GenderfliudDie(4, sprites),

            'd20_genderqueer': Die(range(1,21), sprites['d20_genderqueer']),
            'd12_genderqueer': Die(range(1,13), sprites['d12_genderqueer']),
            'd10_genderqueer': Die(range(1,11), sprites['d10_genderqueer']),
            'd8_genderqueer': Die(range(1,9), sprites['d8_genderqueer']),
            'd6_genderqueer': Die(range(1,7), sprites['d6_genderqueer']),
            'd4_genderqueer': Die(range(1,5), sprites['d4_genderqueer']),

            'd20_nonbinary': NonBinaryDie(20, sprites['d20_nonbinary']),
            'd12_nonbinary': NonBinaryDie(12, sprites['d12_nonbinary']),
            'd10_nonbinary': NonBinaryDie(10, sprites['d10_nonbinary']),
            'd8_nonbinary': NonBinaryDie(8, sprites['d8_nonbinary']),
            'd6_nonbinary': NonBinaryDie(6, sprites['d6_nonbinary']),
            'd4_nonbinary': NonBinaryDie(4, sprites['d4_nonbinary']),

            'd20_rainbow': Die(range(1,21), sprites['d20_rainbow']),
            'd12_rainbow': Die(range(1,13), sprites['d12_rainbow']),
            'd10_rainbow': Die(range(1,11), sprites['d10_rainbow']),
            'd8_rainbow': Die(range(1,9), sprites['d8_rainbow']),
            'd6_rainbow': Die(range(1,7), sprites['d6_rainbow']),
            'd4_rainbow': Die(range(1,5), sprites['d4_rainbow']),

            'd20_trans': Die(range(1,21), sprites['d20_trans']),
            'd12_trans': Die(range(1,13), sprites['d12_trans']),
            'd10_trans': Die(range(1,11), sprites['d10_trans']),
            'd8_trans': Die(range(1,9), sprites['d8_trans']),
            'd6_trans': Die(range(1,7), sprites['d6_trans']),
            'd4_trans': Die(range(1,5), sprites['d4_trans']),

            'd20_purple_pink': Die(range(1,21), sprites['d20_purple_pink']),
            'd12_purple_pink': Die(range(1,13), sprites['d12_purple_pink']),
            'd10_purple_pink': Die(range(1,11), sprites['d10_purple_pink']),
            'd8_purple_pink': Die(range(1,9), sprites['d8_purple_pink']),
            'd6_purple_pink': Die(range(1,7), sprites['d6_purple_pink']),
            'd4_purple_pink': Die(range(1,5), sprites['d4_purple_pink']),

            'd20_red_yellow': Die(range(1,21), sprites['d20_red_yellow']),
            'd12_red_yellow': Die(range(1,13), sprites['d12_red_yellow']),
            'd10_red_yellow': Die(range(1,11), sprites['d10_red_yellow']),
            'd8_red_yellow': Die(range(1,9), sprites['d8_red_yellow']),
            'd6_red_yellow': Die(range(1,7), sprites['d6_red_yellow']),
            'd4_red_yellow': Die(range(1,5), sprites['d4_red_yellow']),
        }
        return dice[name]
    

class GenderfliudDie(Die):
    def __init__(self, n_sides: int, sprites: dict[str, Sprite]):
        self.sprites = sprites 
        self.n_sides = n_sides
        super().__init__(range(1, n_sides + 1), self.get_sprite(n_sides))

    def roll(self) -> int:
        options = [4, 6, 8, 10, 12, 20]
        n_sides = random.choice(options)
        self.sprite = self.get_sprite(n_sides)
        value = random.choice(range(1, n_sides + 1))
        self.last_roll = value
        return value

    def get_sprite(self, n_sides: int) -> Sprite:
        return self.sprites[f"d{n_sides}_genderfluid"]
    

class NonBinaryDie(Die):
    def __init__(self, n_sides: int, sprite: Sprite):
        super().__init__(range(1, n_sides + 1), sprite)

    def roll(self) -> int:
        while True:
            value = random.choice(self.sides)
            if value > 2:
                self.last_roll = value
                return value