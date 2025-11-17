#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import load_sprites
from actors import Actor
from button import Button


def draw_dice(screen, width: int, height: int, box: str, dice: list[Die]) -> None:
    """
    Draw dice in either of the two dice boxes
    """
    if box == 'boss':
        y = height * .2
    elif box == 'player':
        y = height * .575

    count = len(dice)
    if count <= 5:
        deltaX = width * .1
        size = (width * .1, width * .1)
        deltaY = -height * (.05)
    else: # adapt sizes & positions to fit in the same space
        divisor = count / 5

        deltaX = width * .1 / divisor
        size = (deltaX, deltaX)
        deltaY = -height * .05 / divisor

    x = width * .25
    for die in dice:
        y += deltaY
        die.draw(screen, (x, y), scale=size)
        x += deltaX
        deltaY *= -1


def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

    sprites = load_sprites()

    player_dice = [
        Die(range(1,21), sprites['d20_trans']),
        Die(range(1, 13), sprites['d12_trans']),
        Die(range(1, 11), sprites['d10_trans']),
        Die(range(1, 9), sprites['d8_trans']),
        Die(range(1, 7), sprites['d6_trans']),
        Die(range(1, 5), sprites['d4_trans']),
    ]
    player_total = 0
    for die in player_dice:
        player_total += die.roll()

    boss_dice = [
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 7), sprites['d6_white']),
    ]
    boss_total = 0
    for die in boss_dice:
        boss_total += die.roll()

    ui_sections = [
        ((200, 0, 0), (0, 0, width * .2, height * .375), "spooky boss art"),
        ((200, 0, 0), (width * .8, 0, width * .2, height * .375), "boss dice bag"),

        ((0, 200, 0), (0, height * .375, width * .2, height * .375), "player stats/art?"),
        ((0, 200, 0), (width * .8, height * .375, width * .2, height * .375), "player dice bag"),

        ((0, 0, 200), (0, height * .75, width * .2, height * .25), "game options?"),
        ((0, 0, 100), (width * .2, height * .75, width * .6, height * .25), "attack options"),
        ((0, 0, 200), (width * .8, height * .75, width * .2, height * .25), "game options?"),
    ]

    player = Actor(
        'player',
        sprites['art_boss'],
        sprites['dice_box_player'],
        DiceBag(player_dice, sprites['dice_bag']),
    )

    boss = Actor(
        'boss',
        sprites['art_boss'],
        sprites['dice_box_boss'],
        DiceBag(boss_dice, sprites['dice_bag'])
    )

    buttons = []

    num_attacks = 5
    x_mult = .2
    for i in range(num_attacks):
        button = Button(
            f"atk {i}",
            (width * x_mult, height * .8),
            (width * .1, height * .1),
            sprites['button_attack']
        )
        buttons.append(button)
        x_mult += .125

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.inside(pos):
                        print(f"clicked {btn.label}")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        boss.dice_box_art.draw(screen, (width * .2, 0), scale = (width * .6, height * .375))
        label = font.render(str(boss_total), False, (0, 0, 0))
        label = pygame.transform.scale(label, (width * .1, height * .1))
        screen.blit(label, (width * .45, height * .05))

        player.dice_box_art.draw(screen, (width * .2, height * .375), scale = (width * .6, height * .375))
        label = font.render(str(player_total), False, (0, 0, 0))
        label = pygame.transform.scale(label, (width * .1, height * .1))
        screen.blit(label, (width * .45, height * .425))

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            screen.blit(label, (w, h))


        boss.dice_bag.draw(screen, (width * .8, height * .475), scale = (width * .225, height * .225))
        player.dice_bag.draw(screen, (width * .8, height * .1), scale = (width * .225, height * .225))

        boss.profile_art.draw(screen, (0, height * .1), scale = (width * .225, height * .225))

        for btn in buttons:
            btn.draw(screen)

        draw_dice(screen, width, height, 'boss', boss_dice)
        draw_dice(screen, width, height, 'player', player_dice)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
