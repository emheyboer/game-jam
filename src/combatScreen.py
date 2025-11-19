import pygame

from dice import Die
from diceBag import DiceBag
from attack import Attack
from actors import Actor
from button import Button
from screen import Screen
from sprites import Sprite
from shopScreen import shopScreen

class combatScreen(Screen):
    def __init__(self, screen, width: int, height: int, sprites: dict[str, Sprite]) -> None:
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
        
        toShop_Button = Button(
            label = "To Shop!",
            pos = (width * .8, height * .75),
            size = (width * .20, height * .20),
            sprite = sprites['button_toShop'],
            kind = 'navigation'
        )
        self.buttons.append(toShop_Button)
        self.roundWon = False
        self.take_turn()


    def init_player(self) -> None:
        player_dice_bag = DiceBag([
            Die.predefined(self.sprites, 'd20_genderfluid'),
            Die.predefined(self.sprites, 'd12_genderfluid'),
            Die.predefined(self.sprites, 'd10_genderfluid'),
            Die.predefined(self.sprites, 'd8_genderfluid'),
            Die.predefined(self.sprites, 'd6_genderfluid'),
            Die.predefined(self.sprites, 'd4_genderfluid'),
            Die.predefined(self.sprites, 'd20_nonbinary'),
            Die.predefined(self.sprites, 'd12_nonbinary'),
            Die.predefined(self.sprites, 'd10_nonbinary'),
            Die.predefined(self.sprites, 'd8_nonbinary'),
            Die.predefined(self.sprites, 'd6_nonbinary'),
            Die.predefined(self.sprites, 'd4_nonbinary'),
            Die.predefined(self.sprites, 'd20_white'),
            Die.predefined(self.sprites, 'd12_white'),
            Die.predefined(self.sprites, 'd10_white'),
            Die.predefined(self.sprites, 'd8_white'),
            Die.predefined(self.sprites, 'd6_white'),
            Die.predefined(self.sprites, 'd4_white'),
            Die.predefined(self.sprites, 'd20_rainbow'),
            Die.predefined(self.sprites, 'd12_rainbow'),
            Die.predefined(self.sprites, 'd10_rainbow'),
            Die.predefined(self.sprites, 'd8_rainbow'),
            Die.predefined(self.sprites, 'd6_rainbow'),
            Die.predefined(self.sprites, 'd4_rainbow'),
            Die.predefined(self.sprites, 'd20_blue_green'),
            Die.predefined(self.sprites, 'd12_blue_green'),
            Die.predefined(self.sprites, 'd10_blue_green'),
            Die.predefined(self.sprites, 'd8_blue_green'),
            Die.predefined(self.sprites, 'd6_blue_green'),
            Die.predefined(self.sprites, 'd4_blue_green'),
            Die.predefined(self.sprites, 'd20_inverted'),
            Die.predefined(self.sprites, 'd12_inverted'),
            Die.predefined(self.sprites, 'd10_inverted'),
            Die.predefined(self.sprites, 'd8_inverted'),
            Die.predefined(self.sprites, 'd6_inverted'),
            Die.predefined(self.sprites, 'd4_inverted'),
            Die.predefined(self.sprites, 'd20_pink_blue'),
            Die.predefined(self.sprites, 'd12_pink_blue'),
            Die.predefined(self.sprites, 'd10_pink_blue'),
            Die.predefined(self.sprites, 'd8_pink_blue'),
            Die.predefined(self.sprites, 'd6_pink_blue'),
            Die.predefined(self.sprites, 'd4_pink_blue'),
            Die.predefined(self.sprites, 'd20_brown_yellow'),
            Die.predefined(self.sprites, 'd12_brown_yellow'),
            Die.predefined(self.sprites, 'd10_brown_yellow'),
            Die.predefined(self.sprites, 'd8_brown_yellow'),
            Die.predefined(self.sprites, 'd6_brown_yellow'),
            Die.predefined(self.sprites, 'd4_brown_yellow'),
            Die.predefined(self.sprites, 'd20_red_yellow'),
            Die.predefined(self.sprites, 'd12_red_yellow'),
            Die.predefined(self.sprites, 'd10_red_yellow'),
            Die.predefined(self.sprites, 'd8_red_yellow'),
            Die.predefined(self.sprites, 'd6_red_yellow'),
            Die.predefined(self.sprites, 'd4_red_yellow'),
            Die.predefined(self.sprites, 'd20_agender'),
            Die.predefined(self.sprites, 'd12_agender'),
            Die.predefined(self.sprites, 'd10_agender'),
            Die.predefined(self.sprites, 'd8_agender'),
            Die.predefined(self.sprites, 'd6_agender'),
            Die.predefined(self.sprites, 'd4_agender'),
            Die.predefined(self.sprites, 'd20_genderqueer'),
            Die.predefined(self.sprites, 'd12_genderqueer'),
            Die.predefined(self.sprites, 'd10_genderqueer'),
            Die.predefined(self.sprites, 'd8_genderqueer'),
            Die.predefined(self.sprites, 'd6_genderqueer'),
            Die.predefined(self.sprites, 'd4_genderqueer'),
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
            Die.predefined(self.sprites, 'd20_genderfluid'),
            Die.predefined(self.sprites, 'd12_genderfluid'),
            Die.predefined(self.sprites, 'd10_genderfluid'),
            Die.predefined(self.sprites, 'd8_genderfluid'),
            Die.predefined(self.sprites, 'd6_genderfluid'),
            Die.predefined(self.sprites, 'd4_genderfluid'),
            Die.predefined(self.sprites, 'd20_nonbinary'),
            Die.predefined(self.sprites, 'd12_nonbinary'),
            Die.predefined(self.sprites, 'd10_nonbinary'),
            Die.predefined(self.sprites, 'd8_nonbinary'),
            Die.predefined(self.sprites, 'd6_nonbinary'),
            Die.predefined(self.sprites, 'd4_nonbinary'),
            Die.predefined(self.sprites, 'd20_white'),
            Die.predefined(self.sprites, 'd12_white'),
            Die.predefined(self.sprites, 'd10_white'),
            Die.predefined(self.sprites, 'd8_white'),
            Die.predefined(self.sprites, 'd6_white'),
            Die.predefined(self.sprites, 'd4_white'),
            Die.predefined(self.sprites, 'd20_rainbow'),
            Die.predefined(self.sprites, 'd12_rainbow'),
            Die.predefined(self.sprites, 'd10_rainbow'),
            Die.predefined(self.sprites, 'd8_rainbow'),
            Die.predefined(self.sprites, 'd6_rainbow'),
            Die.predefined(self.sprites, 'd4_rainbow'),
            Die.predefined(self.sprites, 'd20_blue_green'),
            Die.predefined(self.sprites, 'd12_blue_green'),
            Die.predefined(self.sprites, 'd10_blue_green'),
            Die.predefined(self.sprites, 'd8_blue_green'),
            Die.predefined(self.sprites, 'd6_blue_green'),
            Die.predefined(self.sprites, 'd4_blue_green'),
            Die.predefined(self.sprites, 'd20_inverted'),
            Die.predefined(self.sprites, 'd12_inverted'),
            Die.predefined(self.sprites, 'd10_inverted'),
            Die.predefined(self.sprites, 'd8_inverted'),
            Die.predefined(self.sprites, 'd6_inverted'),
            Die.predefined(self.sprites, 'd4_inverted'),
            Die.predefined(self.sprites, 'd20_pink_blue'),
            Die.predefined(self.sprites, 'd12_pink_blue'),
            Die.predefined(self.sprites, 'd10_pink_blue'),
            Die.predefined(self.sprites, 'd8_pink_blue'),
            Die.predefined(self.sprites, 'd6_pink_blue'),
            Die.predefined(self.sprites, 'd4_pink_blue'),
            Die.predefined(self.sprites, 'd20_brown_yellow'),
            Die.predefined(self.sprites, 'd12_brown_yellow'),
            Die.predefined(self.sprites, 'd10_brown_yellow'),
            Die.predefined(self.sprites, 'd8_brown_yellow'),
            Die.predefined(self.sprites, 'd6_brown_yellow'),
            Die.predefined(self.sprites, 'd4_brown_yellow'),
            Die.predefined(self.sprites, 'd20_red_yellow'),
            Die.predefined(self.sprites, 'd12_red_yellow'),
            Die.predefined(self.sprites, 'd10_red_yellow'),
            Die.predefined(self.sprites, 'd8_red_yellow'),
            Die.predefined(self.sprites, 'd6_red_yellow'),
            Die.predefined(self.sprites, 'd4_red_yellow'),
            Die.predefined(self.sprites, 'd20_agender'),
            Die.predefined(self.sprites, 'd12_agender'),
            Die.predefined(self.sprites, 'd10_agender'),
            Die.predefined(self.sprites, 'd8_agender'),
            Die.predefined(self.sprites, 'd6_agender'),
            Die.predefined(self.sprites, 'd4_agender'),
            Die.predefined(self.sprites, 'd20_genderqueer'),
            Die.predefined(self.sprites, 'd12_genderqueer'),
            Die.predefined(self.sprites, 'd10_genderqueer'),
            Die.predefined(self.sprites, 'd8_genderqueer'),
            Die.predefined(self.sprites, 'd6_genderqueer'),
            Die.predefined(self.sprites, 'd4_genderqueer'),
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
        self.player_total, boss_poisoned, self.player_dice = self.player.roll_attack(atk_index=atkPlayer)
        self.boss_total, player_poisoned, self.boss_dice = self.boss.roll_attack(atk_index=atkBoss)

        if boss_poisoned:
            for die in self.boss_dice:
                die.last_roll -= 1
            self.boss_total -= len(self.boss_dice)
        if player_poisoned:
            for die in self.player_dice:
                die.last_roll -= 1
            self.player_total -= len(self.player_dice)

        # only the winner's dice are re-added to their bag (or both in the case of a tie)
        if self.player_total >= self.boss_total:
            self.player.dice_bag.add_dice(self.player_dice)
        if self.boss_total >= self.player_total:
            self.boss.dice_bag.add_dice(self.boss_dice)

        for btn in self.buttons:
            if btn.kind == 'attack' and not self.player.attacks[btn.value].is_possible(self.player.dice_bag):
                self.buttons.remove(btn)

        if self.player.next_attack() is None:
            print("you lose :(")
            self.roundWon = False
        elif self.boss.next_attack() is None:
            print("you win :)")
            self.roundWon = True
    
    def on_event(self, event) -> Screen:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for btn in self.buttons:
                if btn.inside(pos) and btn.kind == 'attack':
                    self.take_turn(atkPlayer=btn.value)
                    print(f"player has {self.player.dice_bag.size()} dice, boss has {self.boss.dice_bag.size()} dice")
                    break

                # Change self.roundWon == True: when ready to play set to false for testing
                if btn.inside(pos) and btn.kind == 'navigation' and self.roundWon == False:
                    return shopScreen(self.screen, self.width, self.height, self.sprites)                

        return self