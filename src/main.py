#!/usr/bin/env python3
import pygame

from sprites import load_sprites
from combatScreen import combatScreen
from shopScreen import shopScreen
from dice import Die
from diceBag import DiceBag
from actors import Actor
from attack import Attack
from lossScreen import lossScreen


def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    clock = pygame.time.Clock()

    sprites = load_sprites()

    player_dice_bag = DiceBag([
        Die.predefined(sprites, 'd20_basic'),
        Die.predefined(sprites, 'd12_basic'),
        Die.predefined(sprites, 'd10_basic'),
        Die.predefined(sprites, 'd8_basic'),
        Die.predefined(sprites, 'd6_basic'),
    ], sprites['dice_bag'])

    player_attacks = [
        # Attack([], gambling=True),
        Attack([(1, 20)]),
        Attack([(2, 12)]),
        Attack([(3, 10)]),
        Attack([(4, 8)]),
        Attack([(5, 6)]),
    ]

    player = Actor(
        'player',
        sprites['dice_goblin'],
        sprites['dice_box_player'],
        player_dice_bag,
        player_attacks,
    )

    current_screen = combatScreen(screen, width, height, sprites, player, 0)
    # ~~~ Testing Purposes ~~~
    #current_screen = shopScreen(screen, width, height, sprites, player, 0)
    #current_screen = lossScreen(screen, width, height, sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                current_screen = current_screen.on_event(event)

                if current_screen == "retry":
                    return main()

                

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        current_screen.draw()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
