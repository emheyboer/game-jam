#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import load_sprites


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
        Die(range(1, 21), sprites['d20_white']),
        Die(range(1, 13), sprites['d12_white']),
        Die(range(1, 11), sprites['d10_white']),
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 5), sprites['d4_white']),
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

    player_dice_bag = DiceBag(player_dice, sprites['dice_bag'])
    boss_dice_bag = DiceBag(boss_dice, sprites['dice_bag'])

    attack_btn = sprites['button_attack']
    num_attacks = 5


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        sprites['dice_box_boss'].draw(screen, width * .2, 0, scale = (width * .6, height * .375))
        label = font.render(str(boss_total), False, (0, 0, 0))
        label = pygame.transform.scale(label, (width * .1, height * .1))
        screen.blit(label, (width * .45, height * .05))

        sprites['dice_box_player'].draw(screen, width * .2, height * .375, scale = (width * .6, height * .375))
        label = font.render(str(player_total), False, (0, 0, 0))
        label = pygame.transform.scale(label, (width * .1, height * .1))
        screen.blit(label, (width * .45, height * .425))

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            screen.blit(label, (w, h))


        boss_dice_bag.draw(screen, width * .8, height * .475, scale = (width * .225, height * .225))
        player_dice_bag.draw(screen, width * .8, height * .1, scale = (width * .225, height * .225))

        sprites['art_boss'].draw(screen, 0, height * .1, scale = (width * .225, height * .225))

        x_mult = .2
        for i in range(num_attacks):
            attack_btn.draw(screen, width * x_mult, height * .8, scale = (width * .1, height * .1))
            x_mult += .125

        x = width * .25 
        for die in boss_dice:
            die.draw(screen, x, height * .2)
            x += 128

        x = width * .25
        for die in player_dice:
            die.draw(screen, x, height * .575)
            x += 128

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
