#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import load_sprites
from actors import Actor
from button import Button
from attack import Attack
from combatScreen import combatScreen


def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    clock = pygame.time.Clock()

    sprites = load_sprites()

    current_screen = combatScreen(screen, width, height, sprites)

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
