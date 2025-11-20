import pygame

class SpriteSheet:
    def __init__(self, path: str) -> None:
        self.path = path
        self.surface = pygame.image.load(path).convert()


class Sprite:
    def __init__(self, spriteSheet: SpriteSheet, pos: tuple[int, int], size: tuple[int, int],
                 textOffset: tuple[int, int] = (0, 0), fontSize: int = 30) -> None:
        self.spriteSheet = spriteSheet
        self.x, self.y = pos
        self.width, self.height = size
        self.offsetX, self.offsetY = textOffset
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), fontSize)

        self.sprite = pygame.Surface(size)
        self.sprite.set_colorkey((0,0,0))
        self.sprite.blit(self.spriteSheet.surface, (0, 0), (self.x, self.y, self.width, self.height))

    def draw(self, screen, pos: tuple[float, float], size = None, text = None, scaleText: bool = True):
        x, y = pos
        sprite = self.sprite.copy()
        
        if text is not None and scaleText:
            text_surface = self.font.render(text, False, (1, 1, 1))
            sprite.blit(text_surface, (self.offsetX, self.offsetY))

        if size is not None:
            sprite = pygame.transform.scale(sprite, size)

        if text is not None and not scaleText:
            text_surface = self.font.render(text, False, (1, 1, 1))
            sprite.blit(text_surface, (self.offsetX, self.offsetY))

        screen.blit(sprite, (x, y))


def load_sprites():
    sprites = {}

    dice_sprite_sheets = [
        ('white', 'assets/dice/Small/small_dice.png'),
        ('blue_green', 'assets/dice/Small/small_dice_bluegreen.png'),
        ('brown_yellow', 'assets/dice/Small/small_dice_brownyellow.png'),
        ('inverted', 'assets/dice/Small/small_dice_inverted.png'),
        ('pink_blue', 'assets/dice/Small/small_dice_pinkblue.png'),
        ('agender', 'assets/dice/Small/small_dice_pride_agender.png'),
        ('genderfluid', 'assets/dice/Small/small_dice_pride_genderfluid.png'),
        ('genderqueer', 'assets/dice/Small/small_dice_pride_genderqueer.png'),
        ('nonbinary', 'assets/dice/Small/small_dice_pride_nonbinary.png'),
        ('rainbow', 'assets/dice/Small/small_dice_pride_rainbow.png'),
        ('trans', 'assets/dice/Small/small_dice_pride_trans.png'),
        ('purple_pink', 'assets/dice/Small/small_dice_purplepink.png'),
        ('red_yellow', 'assets/dice/Small/small_dice_redyellow.png'),
    ]
    dice_sprites_positions = [
        # (name, position, size, text offset)
        ('d20', (15, 15), (104, 103), (48, 30)),
        ('d12', (142, 15), (99, 103), (35, 40)),
        ('d10', (265, 23), (92, 88), (40, 32)),
        ('d8', (494, 18), (98, 96), (55, 30)),
        ('d6', (617, 21), (94, 93), (60, 32)),
        ('d4', (739, 31), (75, 82), (32, 25))
    ]

    for variant, path in dice_sprite_sheets:
        sheet = SpriteSheet(path)
        for die, pos, size, offset in dice_sprites_positions:
            sprites[f"{die}_{variant}"] = Sprite(sheet, pos, size, textOffset=offset)
        
    dice_box = Sprite(
        SpriteSheet('assets/ui/PNG/panel_brown.png'),
        (0, 0),
        (100, 100),
        textOffset=(40, 10)
    )
    sprites['dice_box_player'] = dice_box
    sprites['dice_box_boss'] = dice_box

    inventory = SpriteSheet('assets/inventory/sprites.png')
    sprites['dice_bag'] = Sprite(inventory, (64, 16), (16, 16))

    sprites['bug_girl'] = Sprite(
        SpriteSheet('assets/boss/bug_girl.png'),
        (0, 0),
        (1515, 1515)
    )

    sprites['dice_goblin'] = Sprite(
        SpriteSheet('assets/boss/dice_goblin.png'),
        (0, 0),
        (2807, 2806),
    )

    sprites['emiotter'] = Sprite(
        SpriteSheet('assets/boss/emiotter.png'),
        (0, 0),
        (4324, 4324)
    )

    sprites['goat_girl'] = Sprite(
        SpriteSheet('assets/boss/goat_girl.png'),
        (0, 0),
        (1378, 1378)
    )

    sprites['necromancer'] = Sprite(
        SpriteSheet('assets/boss/necromancer.png'),
        (0, 0),
        (1487, 1487)
    )

    sprites['slime_blue'] = Sprite(
        SpriteSheet('assets/boss/blue_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['slime_colon_three'] = Sprite(
        SpriteSheet('assets/boss/slime_colon_three.png'),
        (0, 0),
        (1355, 1355)
    )

    sprites['slime_green'] = Sprite(
        SpriteSheet('assets/boss/green_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['slime_orange'] = Sprite(
        SpriteSheet('assets/boss/orange_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['slime_pink'] = Sprite(
        SpriteSheet('assets/boss/pink_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['slime_red'] = Sprite(
        SpriteSheet('assets/boss/red_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['slime_yellow'] = Sprite(
        SpriteSheet('assets/boss/yellow_dice_slime_transparent.png'),
        (0, 0),
        (2048, 2048)
    )

    sprites['tootle'] = Sprite(
        SpriteSheet('assets/boss/tootle.png'),
        (0, 0),
        (2725, 2725)
    )

    sprites['vesphira'] = Sprite(
        SpriteSheet('assets/boss/vesphira.png'),
        (0, 0),
        (3349, 3349)
    )

    sprites['button_attack'] = Sprite(
        SpriteSheet('assets/ui/PNG/buttonSquare_blue.png'),
        (0, 0), (45, 49), textOffset=(15, 20),
        fontSize=75
    )

    sprites['background'] = Sprite(
        SpriteSheet('assets/wood/Wood Texture 2.png'),
        (0, 0), (2048, 2048), textOffset=(5, 15),
        fontSize=20
    )

    button_toShop = Sprite(
        SpriteSheet('assets/ui/PNG/buttonSquare_blue.png'),
        (0, 0), (45, 49), textOffset=(25, 50),
        fontSize=75
    )
    sprites['button_toShop'] = button_toShop

    shopButton = Sprite(
        SpriteSheet('assets/ui/PNG/buttonSquare_brown.png'),
        (0, 0), (45, 49), textOffset=(50, 10),
        fontSize=50
    )
    sprites['shopButton'] = shopButton

    sprites['background_Loss'] = Sprite(
        SpriteSheet('assets/ui/Youlose.png'),
        (0, 0), (1440, 900), textOffset=(5, 15),
        fontSize=20
    )

    sprites['gold'] = Sprite(
        SpriteSheet('assets/ui/Coin.png'),
        (0, 0), (550, 550), textOffset=(5, 15),
        fontSize=20
    )
    return sprites
