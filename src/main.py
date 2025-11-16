#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import SpriteSheet, Sprite

WIDTH = 1024
HEIGHT = 768

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

    sheet = SpriteSheet('assets/dice/Small/small_dice_pride_trans.png')

    d20_sprite = Sprite(sheet, (0, 0), (128, 128))
    d20 = Die([i for  i in range(1, 21)], d20_sprite, (64, 45))

    d12_sprite = Sprite(sheet, (128, 0), (128, 128))
    d12 = Die([i for  i in range(1, 13)], d12_sprite, (50, 50))

    d10_sprite = Sprite(sheet, (256, 0), (128, 128))
    d10 = Die([i for  i in range(1, 11)], d10_sprite, (50, 50))

    d8_sprite = Sprite(sheet, (500, 0), (100, 128))
    d8 = Die([i for  i in range(1, 9)], d8_sprite, (50, 50))

    d6_sprite = Sprite(sheet, (620, 0), (120, 128))
    d6 = Die([i for  i in range(1, 7)], d6_sprite, (60, 55))

    d4_sprite = Sprite(sheet, (728, 0), (100, 128))
    d4 = Die([i for  i in range(1, 7)], d4_sprite, (40, 55))

    dice = [d20, d12, d10, d8, d6, d4]

    for die in dice:
        die.roll()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 0, 0), (0, 0, WIDTH, HEIGHT))
        # screen.blit(dice.sheet, (100, 0))

        x, y = 0, 0
        for die in dice:
            die.draw(screen, x, y)
            x += 128

        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
