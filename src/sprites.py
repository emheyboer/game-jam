import pygame

class SpriteSheet:
    def __init__(self, path: str) -> None:
        self.path = path
        self.surface = pygame.image.load(path)


class Sprite:
    def __init__(self, spriteSheet: SpriteSheet, pos: tuple[int, int], size: tuple[int, int]) -> None:
        self.spriteSheet = spriteSheet
        self.x, self.y = pos
        self.width, self.height = size

        self.sprite = pygame.Surface(size)
        self.sprite.set_colorkey((0,0,0))
        self.sprite.blit(self.spriteSheet.surface, (0, 0), (self.x, self.y, self.width, self.height))

    def draw(self, screen, x: float, y: float, scale = None):
        sprite = self.sprite
        if scale:
            sprite = pygame.transform.scale(sprite, scale)
        screen.blit(sprite, (x, y))


def load_sprites():
    sprites = {}

    dice_sprite_sheets = [
        ('trans', 'assets/dice/Small/small_dice_pride_trans.png'),
        ('white', 'assets/dice/Small/small_dice.png')
    ]
    dice_sprites_positions = [
        ('d20', (0, 0), (128, 128)),
        ('d12', (128, 0), (128, 128)),
        ('d10', (256, 0), (128, 128)),
        # some of these are definitely off
        ('d8', (500, 0), (100, 128)),
        ('d6', (620, 0), (120, 128)),
        ('d4', (728, 0), (100, 128))
    ]

    for variant, path in dice_sprite_sheets:
        sheet = SpriteSheet(path)
        for die, pos, size in dice_sprites_positions:
            sprites[f"{die}_{variant}"] = Sprite(sheet, pos, size)
        
    dice_box = Sprite(SpriteSheet('assets/ui/PNG/panel_brown.png'), (0, 0), (100, 100))
    sprites['dice_box_player'] = dice_box
    sprites['dice_box_boss'] = dice_box

    inventory = SpriteSheet('assets/inventory/sprites.png')
    sprites['art_boss'] = Sprite(inventory, (16 * 5, 16 * 7), (16, 16))
    sprites['dice_bag'] = Sprite(inventory, (64, 16), (16, 16))

    sprites['button_attack'] = Sprite(SpriteSheet('assets/ui/PNG/buttonSquare_blue.png'), (0, 0), (45, 49))

    return sprites
