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
        Die.predefined(sprites, 'd20_fluid'),
        Die.predefined(sprites, 'd12_fluid'),
        Die.predefined(sprites, 'd10_fluid'),
        Die.predefined(sprites, 'd8_fluid'),
        Die.predefined(sprites, 'd6_fluid'),
        Die.predefined(sprites, 'd4_fluid'),
        Die.predefined(sprites, 'd20_lucky'),
        Die.predefined(sprites, 'd12_lucky'),
        Die.predefined(sprites, 'd10_lucky'),
        Die.predefined(sprites, 'd8_lucky'),
        Die.predefined(sprites, 'd6_lucky'),
        Die.predefined(sprites, 'd4_lucky'),
        Die.predefined(sprites, 'd20_basic'),
        Die.predefined(sprites, 'd12_basic'),
        Die.predefined(sprites, 'd10_basic'),
        Die.predefined(sprites, 'd8_basic'),
        Die.predefined(sprites, 'd6_basic'),
        Die.predefined(sprites, 'd4_basic'),
        Die.predefined(sprites, 'd20_exploding'),
        Die.predefined(sprites, 'd12_exploding'),
        Die.predefined(sprites, 'd10_exploding'),
        Die.predefined(sprites, 'd8_exploding'),
        Die.predefined(sprites, 'd6_exploding'),
        Die.predefined(sprites, 'd4_exploding'),
        Die.predefined(sprites, 'd20_glass'),
        Die.predefined(sprites, 'd12_glass'),
        Die.predefined(sprites, 'd10_glass'),
        Die.predefined(sprites, 'd8_glass'),
        Die.predefined(sprites, 'd6_glass'),
        Die.predefined(sprites, 'd4_glass'),
        Die.predefined(sprites, 'd20_union'),
        Die.predefined(sprites, 'd12_union'),
        Die.predefined(sprites, 'd10_union'),
        Die.predefined(sprites, 'd8_union'),
        Die.predefined(sprites, 'd6_union'),
        Die.predefined(sprites, 'd4_union'),
        Die.predefined(sprites, 'd20_advantage'),
        Die.predefined(sprites, 'd12_advantage'),
        Die.predefined(sprites, 'd10_advantage'),
        Die.predefined(sprites, 'd8_advantage'),
        Die.predefined(sprites, 'd6_advantage'),
        Die.predefined(sprites, 'd4_advantage'),
        Die.predefined(sprites, 'd20_stone'),
        Die.predefined(sprites, 'd12_stone'),
        Die.predefined(sprites, 'd10_stone'),
        Die.predefined(sprites, 'd8_stone'),
        Die.predefined(sprites, 'd6_stone'),
        Die.predefined(sprites, 'd4_stone'),
        Die.predefined(sprites, 'd20_fire'),
        Die.predefined(sprites, 'd12_fire'),
        Die.predefined(sprites, 'd10_fire'),
        Die.predefined(sprites, 'd8_fire'),
        Die.predefined(sprites, 'd6_fire'),
        Die.predefined(sprites, 'd4_fire'),
        Die.predefined(sprites, 'd20_poison'),
        Die.predefined(sprites, 'd12_poison'),
        Die.predefined(sprites, 'd10_poison'),
        Die.predefined(sprites, 'd8_poison'),
        Die.predefined(sprites, 'd6_poison'),
        Die.predefined(sprites, 'd4_poison'),
        Die.predefined(sprites, 'd20_outlier'),
        Die.predefined(sprites, 'd12_outlier'),
        Die.predefined(sprites, 'd10_outlier'),
        Die.predefined(sprites, 'd8_outlier'),
        Die.predefined(sprites, 'd6_outlier'),
        Die.predefined(sprites, 'd4_outlier'),
        Die.predefined(sprites, 'd20_money'),
        Die.predefined(sprites, 'd12_money'),
        Die.predefined(sprites, 'd10_money'),
        Die.predefined(sprites, 'd8_money'),
        Die.predefined(sprites, 'd6_money'),
        Die.predefined(sprites, 'd4_money'),
        Die.predefined(sprites, 'd20_trans'),
        Die.predefined(sprites, 'd12_trans'),
        Die.predefined(sprites, 'd10_trans'),
        Die.predefined(sprites, 'd8_trans'),
        Die.predefined(sprites, 'd6_trans'),
        Die.predefined(sprites, 'd4_trans'),
    ], sprites['dice_bag'])

    player_attacks = [
        Attack([(3, 20)]),
        Attack([(1, 12)]),
        Attack([(2, 10)]),
        Attack([(2, 8)]),
        Attack([(6, 6)]),
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
