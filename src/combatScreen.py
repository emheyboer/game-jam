import pygame

from dice import Die
from diceBag import DiceBag
from attack import Attack
from actors import Actor
from button import Button
from screen import Screen

class combatScreen(Screen):
    def __init__(self, screen, width: int, height: int, sprites) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites

        self.init_player()
        self.init_boss()

        self.buttons = []

        x_mult = .2
        for i in range(len(self.player.attacks)):
            button = Button(
                f"{self.player.attacks[i]}",
                (width * x_mult, height * .8),
                (width * .1, height * .1),
                sprites['button_attack'],
                'attack',
                value=i
            )
            self.buttons.append(button)
            x_mult += .125
        
        self.take_turn()


    def init_player(self) -> None:
        player_dice_bag = DiceBag([
            Die(range(1,21), self.sprites['d20_trans']),
            Die(range(1, 13), self.sprites['d12_trans']),
            Die(range(1, 11), self.sprites['d10_trans']),
            Die(range(1, 9), self.sprites['d8_trans']),
            Die(range(1, 7), self.sprites['d6_trans']),
            Die(range(1, 5), self.sprites['d4_trans']),
            Die(range(1,21), self.sprites['d20_trans']),
            Die(range(1, 13), self.sprites['d12_trans']),
            Die(range(1, 11), self.sprites['d10_trans']),
            Die(range(1, 9), self.sprites['d8_trans']),
            Die(range(1, 7), self.sprites['d6_trans']),
            Die(range(1, 5), self.sprites['d4_trans']),
            Die(range(1,21), self.sprites['d20_trans']),
            Die(range(1, 13), self.sprites['d12_trans']),
            Die(range(1, 11), self.sprites['d10_trans']),
            Die(range(1, 9), self.sprites['d8_trans']),
            Die(range(1, 7), self.sprites['d6_trans']),
            Die(range(1, 5), self.sprites['d4_trans']),
        ], self.sprites['dice_bag'])

        player_attacks = [
            Attack([(3, 20)]),
            Attack([(1, 12)]),
            Attack([(2, 10)]),
            Attack([(2, 8)]),
            Attack([(3, 6)]),
        ]

        self.player = Actor(
            'player',
            self.sprites['art_boss'],
            self.sprites['dice_box_player'],
            player_dice_bag,
            player_attacks,
        )

    def init_boss(self) -> None:
        boss_dice_bag = DiceBag([
            Die(range(1,21), self.sprites['d20_white']),
            Die(range(1, 13), self.sprites['d12_white']),
            Die(range(1, 11), self.sprites['d10_white']),
            Die(range(1, 9), self.sprites['d8_white']),
            Die(range(1, 7), self.sprites['d6_white']),
            Die(range(1, 5), self.sprites['d4_white']),
            Die(range(1,21), self.sprites['d20_white']),
            Die(range(1, 13), self.sprites['d12_white']),
            Die(range(1, 11), self.sprites['d10_white']),
            Die(range(1, 9), self.sprites['d8_white']),
            Die(range(1, 7), self.sprites['d6_white']),
            Die(range(1, 5), self.sprites['d4_white']),
            Die(range(1,21), self.sprites['d20_white']),
            Die(range(1, 13), self.sprites['d12_white']),
            Die(range(1, 11), self.sprites['d10_white']),
            Die(range(1, 9), self.sprites['d8_white']),
            Die(range(1, 7), self.sprites['d6_white']),
            Die(range(1, 5), self.sprites['d4_white']),
        ], self.sprites['dice_bag'])
        self.boss = Actor(
            'boss',
            self.sprites['art_boss'],
            self.sprites['dice_box_boss'],
            boss_dice_bag,
            [
                Attack([(2, 8), (3, 6)]),
                Attack([(3, 20)]),
            ],
        )

    def draw(self) -> None:
        width, height = self.width, self.height

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

        self.boss.dice_box_art.draw(self.screen, (width * .2, 0), size = (width * .6, height * .375),
                            text=str(self.boss_total))
        self.player.dice_box_art.draw(self.screen, (width * .2, height * .375), size = (width * .6, height * .375),
                                text=str(self.player_total))

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(self.screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            self.screen.blit(label, (w, h))


        self.boss.dice_bag.draw(self.screen, (width * .8, height * .475), size = (width * .225, height * .225))
        self.player.dice_bag.draw(self.screen, (width * .8, height * .1), size = (width * .225, height * .225))

        self.boss.profile_art.draw(self.screen, (0, height * .1), size = (width * .225, height * .225))

        for btn in self.buttons:
            btn.draw(self.screen)

        self.draw_dice('boss', self.boss_dice)
        self.draw_dice('player', self.player_dice)


    def draw_dice(self, box: str, dice: list[Die]) -> None:
        """
        Draw dice in either of the two dice boxes
        """
        width, height = self.width, self.height

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
            die.draw(self.screen, (x, y), size=size)
            x += deltaX
            deltaY *= -1

    def take_turn(self, atkPlayer: int|None = None, atkBoss: int|None = None) -> None:
        self.player_total, self.player_dice = self.player.roll_attack(atk_index=atkPlayer)
        self.boss_total, self.boss_dice = self.boss.roll_attack(atk_index=atkBoss)

        # only the winner's dice are re-added to their bag (or both in the case of a tie)
        if self.player_total >= self.boss_total:
            self.player.dice_bag.add_dice(self.player_dice)
        if self.boss_total >= self.player_total:
            self.boss.dice_bag.add_dice(self.boss_dice)

        for btn in self.buttons:
            if btn.kind == 'attack' and not self.player.attacks[btn.value].is_possible(self.player.dice_bag):
                self.buttons.remove(btn)
    
    def on_event(self, event) -> Screen:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for btn in self.buttons:
                if btn.inside(pos) and btn.kind == 'attack':
                    self.take_turn(atkPlayer=btn.value)
                    print(f"player = {self.player.dice_bag.size()}, boss = {self.boss.dice_bag.size()}")
                    break

        return self