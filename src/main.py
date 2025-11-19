#!/usr/bin/env python3
import pygame

from sprites import load_sprites
from combatScreen import combatScreen
from shopScreen import shopScreen
from dice import Die
from diceBag import DiceBag
from actors import Actor
from attack import Attack


def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    clock = pygame.time.Clock()

    sprites = load_sprites()

    player_dice_bag = DiceBag([
        Die.predefined(sprites, 'd6_basic'),
        Die.predefined(sprites, 'd6_basic'),
        Die.predefined(sprites, 'd6_basic'),
        Die.predefined(sprites, 'd6_glass'),
        Die.predefined(sprites, 'd6_stone'),
        Die.predefined(sprites, 'd6_advantage'),
        Die.predefined(sprites, 'd6_lucky'),
        Die.predefined(sprites, 'd4_exploding'),
        Die.predefined(sprites, 'd4_poison'),
        Die.predefined(sprites, 'd4_fire'),
    ], sprites['dice_bag'])

    player_attacks = [
        Attack([(3, 6)]),
        Attack([(3, 4)]),
        Attack([(1, 4)]),
    ]

    player = Actor(
        'player',
        sprites['dice_goblin'],
        sprites['dice_box_player'],
        player_dice_bag,
        player_attacks,
    )

    current_screen = combatScreen(screen, width, height, sprites, player, 0)
    #current_screen = shopScreen(screen, width, height, sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                current_screen = current_screen.on_event(event)
                

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
