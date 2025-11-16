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

    def draw(self, screen, x: int, y: int):
        screen.blit(self.sprite, (x, y))
