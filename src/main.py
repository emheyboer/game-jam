#!/usr/bin/env python3
import pygame

from dice import Die
from diceBag import DiceBag
from sprites import load_sprites
from actors import Actor
from button import Button
from attack import Attack


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


def take_turn(actorA: Actor, actorB: Actor,
              atkA: int|None = None, atkB: int|None = None) -> tuple[int, int, list[Die], list[Die]]:
    (totalA, diceA) = actorA.roll_attack(atk_index=atkA)
    (totalB, diceB) = actorB.roll_attack(atk_index=atkB)

    # only the winner's dice are re-added to their bag (or both in the case of a tie)
    if totalA >= totalB:
        actorA.dice_bag.add_dice(diceA)
    if totalB >= totalA:
        actorB.dice_bag.add_dice(diceB)
    

    return (totalA, totalB, diceA, diceB)


def render_combat(screen, width: int, height: int, buttons: list[Button], player: Actor, boss: Actor,
                  player_total: int, boss_total: int, player_dice: list[Die], boss_dice: list[Die]):
    ui_sections = [
        ((200, 0, 0), (0, 0, width * .2, height * .375), "spooky boss art"),
        ((200, 0, 0), (width * .8, 0, width * .2, height * .375), "boss dice bag"),

        ((0, 200, 0), (0, height * .375, width * .2, height * .375), "player stats/art?"),
        ((0, 200, 0), (width * .8, height * .375, width * .2, height * .375), "player dice bag"),

        ((0, 0, 200), (0, height * .75, width * .2, height * .25), "game options?"),
        ((0, 0, 100), (width * .2, height * .75, width * .6, height * .25), "attack options"),
        ((0, 0, 200), (width * .8, height * .75, width * .2, height * .25), "game options?"),
    ]

    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

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


def main():
    pygame.init()

    screen = pygame.display.set_mode()
    width, height = pygame.display.get_surface().get_size()

    clock = pygame.time.Clock()

    sprites = load_sprites()

    player_dice_bag = DiceBag([
        Die(range(1,21), sprites['d20_trans']),
        Die(range(1, 13), sprites['d12_trans']),
        Die(range(1, 11), sprites['d10_trans']),
        Die(range(1, 9), sprites['d8_trans']),
        Die(range(1, 7), sprites['d6_trans']),
        Die(range(1, 5), sprites['d4_trans']),
        Die(range(1,21), sprites['d20_trans']),
        Die(range(1, 13), sprites['d12_trans']),
        Die(range(1, 11), sprites['d10_trans']),
        Die(range(1, 9), sprites['d8_trans']),
        Die(range(1, 7), sprites['d6_trans']),
        Die(range(1, 5), sprites['d4_trans']),
        Die(range(1,21), sprites['d20_trans']),
        Die(range(1, 13), sprites['d12_trans']),
        Die(range(1, 11), sprites['d10_trans']),
        Die(range(1, 9), sprites['d8_trans']),
        Die(range(1, 7), sprites['d6_trans']),
        Die(range(1, 5), sprites['d4_trans']),
    ], sprites['dice_bag'])
    player = Actor(
        'player',
        sprites['art_boss'],
        sprites['dice_box_player'],
        player_dice_bag,
        [
            Attack([(1, 20)]),
            Attack([(1, 12)]),
            Attack([(2, 10)]),
            Attack([(2, 8)]),
            Attack([(3, 6)]),
        ],
    )

    boss_dice_bag = DiceBag([
        Die(range(1,21), sprites['d20_white']),
        Die(range(1, 13), sprites['d12_white']),
        Die(range(1, 11), sprites['d10_white']),
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 5), sprites['d4_white']),
        Die(range(1,21), sprites['d20_white']),
        Die(range(1, 13), sprites['d12_white']),
        Die(range(1, 11), sprites['d10_white']),
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 5), sprites['d4_white']),
        Die(range(1,21), sprites['d20_white']),
        Die(range(1, 13), sprites['d12_white']),
        Die(range(1, 11), sprites['d10_white']),
        Die(range(1, 9), sprites['d8_white']),
        Die(range(1, 7), sprites['d6_white']),
        Die(range(1, 5), sprites['d4_white']),
    ], sprites['dice_bag'])
    boss = Actor(
        'boss',
        sprites['art_boss'],
        sprites['dice_box_boss'],
        boss_dice_bag,
        [
            Attack([(2, 8), (3, 6)]),
            Attack([(3, 20)]),
        ],
    )

    player_total, boss_total, player_dice, boss_dice = take_turn(player, boss)

    buttons = []

    x_mult = .2
    for i in range(len(player.attacks)):
        button = Button(
            f"{player.attacks[i]}",
            (width * x_mult, height * .8),
            (width * .1, height * .1),
            sprites['button_attack'],
            'attack',
            value=i
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
                    if btn.inside(pos) and btn.kind == 'attack':
                        player_total, boss_total, player_dice, boss_dice = take_turn(player, boss, atkA=btn.value)
                        print(f"player = {player.dice_bag.size()}, boss = {boss.dice_bag.size()}")
                        break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            running = False

        screen.fill((0, 0, 0))

        render_combat(screen, width, height, buttons, player, boss,
                      player_total, boss_total, player_dice, boss_dice)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
