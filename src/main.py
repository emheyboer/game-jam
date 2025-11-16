#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import SpriteSheet, Sprite

def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

    sheet = SpriteSheet('assets/dice/Small/small_dice_pride_trans.png')
    player_dice = [
        Die([i for  i in range(1, 21)], Sprite(sheet, (0, 0), (128, 128)), (64, 45)),
        Die([i for  i in range(1, 13)], Sprite(sheet, (128, 0), (128, 128)), (50, 50)),
        Die([i for  i in range(1, 11)], Sprite(sheet, (256, 0), (128, 128)), (50, 50)),
        Die([i for  i in range(1, 9)], Sprite(sheet, (500, 0), (100, 128)), (50, 50)),
        Die([i for  i in range(1, 7)], Sprite(sheet, (620, 0), (120, 128)), (60, 55)),
        Die([i for  i in range(1, 7)], Sprite(sheet, (728, 0), (100, 128)), (40, 55))
    ]
    for die in player_dice:
        die.roll()

    sheet = SpriteSheet('assets/dice/Small/small_dice.png')
    boss_dice = [
        Die([i for  i in range(1, 21)], Sprite(sheet, (0, 0), (128, 128)), (64, 45)),
        Die([i for  i in range(1, 13)], Sprite(sheet, (128, 0), (128, 128)), (50, 50)),
        Die([i for  i in range(1, 11)], Sprite(sheet, (256, 0), (128, 128)), (50, 50)),
        Die([i for  i in range(1, 9)], Sprite(sheet, (500, 0), (100, 128)), (50, 50)),
        Die([i for  i in range(1, 7)], Sprite(sheet, (620, 0), (120, 128)), (60, 55)),
        Die([i for  i in range(1, 7)], Sprite(sheet, (728, 0), (100, 128)), (40, 55))
    ]
    for die in boss_dice:
        die.roll()

    ui_sections = [
        ((200, 0, 0), (0, 0, width * .2, height * .375), "spooky boss art"),
        # ((100, 0, 0), (width * .2, 0, width * .6, height * .375), "boss dice box"),
        ((200, 0, 0), (width * .8, 0, width * .2, height * .375), "boss dice bag"),

        ((0, 200, 0), (0, height * .375, width * .2, height * .375), "player stats/art?"),
        # ((0, 100, 0), (width * .2, height * .375, width * .6, height * .375), "player dice box"),
        ((0, 200, 0), (width * .8, height * .375, width * .2, height * .375), "player dice bag"),

        ((0, 0, 200), (0, height * .75, width * .2, height * .25), "game options?"),
        ((0, 0, 100), (width * .2, height * .75, width * .6, height * .25), "attack options"),
        ((0, 0, 200), (width * .35, height * .8, width * .1, height * .1), "1"),
        ((0, 0, 200), (width * .5, height * .8, width * .1, height * .1), "2"),
        ((0, 0, 200), (width * .65, height * .8, width * .1, height * .1), "3"),
        ((0, 0, 200), (width * .8, height * .75, width * .2, height * .25), "game options?"),
    ]

    player_dice_box = Sprite(SpriteSheet('assets/ui/PNG/panel_brown.png'), (0, 0), (100, 100))
    boss_dice_box = Sprite(SpriteSheet('assets/ui/PNG/panel_brown.png'), (0, 0), (100, 100))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        boss_dice_box.draw(screen, int(width * .2), 0, scale = (width * .6, height * .375))
        player_dice_box.draw(screen, int(width * .2), int(height * .375), scale = (width * .6, height * .375))

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            screen.blit(label, (w + width * .05, h + height * .05))


        x, y = int(width * .25), int(height * .2)
        for die in boss_dice:
            die.draw(screen, x, y)
            x += 128

        x, y = int(width * .25), int(height * .575)
        for die in player_dice:
            die.draw(screen, x, y)
            x += 128

        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
