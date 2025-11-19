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



    def init_player(self) -> None:
        player_dice_bag = DiceBag([
            Die.predefined(self.sprites, 'd20_fluid'),
            Die.predefined(self.sprites, 'd12_fluid'),
            Die.predefined(self.sprites, 'd10_fluid'),
            Die.predefined(self.sprites, 'd8_fluid'),
            Die.predefined(self.sprites, 'd6_fluid'),
            Die.predefined(self.sprites, 'd4_fluid'),
            Die.predefined(self.sprites, 'd20_lucky'),
            Die.predefined(self.sprites, 'd12_lucky'),
            Die.predefined(self.sprites, 'd10_lucky'),
            Die.predefined(self.sprites, 'd8_lucky'),
            Die.predefined(self.sprites, 'd6_lucky'),
            Die.predefined(self.sprites, 'd4_lucky'),
            Die.predefined(self.sprites, 'd20_basic'),
            Die.predefined(self.sprites, 'd12_basic'),
            Die.predefined(self.sprites, 'd10_basic'),
            Die.predefined(self.sprites, 'd8_basic'),
            Die.predefined(self.sprites, 'd6_basic'),
            Die.predefined(self.sprites, 'd4_basic'),
            Die.predefined(self.sprites, 'd20_exploding'),
            Die.predefined(self.sprites, 'd12_exploding'),
            Die.predefined(self.sprites, 'd10_exploding'),
            Die.predefined(self.sprites, 'd8_exploding'),
            Die.predefined(self.sprites, 'd6_exploding'),
            Die.predefined(self.sprites, 'd4_exploding'),
            Die.predefined(self.sprites, 'd20_glass'),
            Die.predefined(self.sprites, 'd12_glass'),
            Die.predefined(self.sprites, 'd10_glass'),
            Die.predefined(self.sprites, 'd8_glass'),
            Die.predefined(self.sprites, 'd6_glass'),
            Die.predefined(self.sprites, 'd4_glass'),
            Die.predefined(self.sprites, 'd20_union'),
            Die.predefined(self.sprites, 'd12_union'),
            Die.predefined(self.sprites, 'd10_union'),
            Die.predefined(self.sprites, 'd8_union'),
            Die.predefined(self.sprites, 'd6_union'),
            Die.predefined(self.sprites, 'd4_union'),
            Die.predefined(self.sprites, 'd20_advantage'),
            Die.predefined(self.sprites, 'd12_advantage'),
            Die.predefined(self.sprites, 'd10_advantage'),
            Die.predefined(self.sprites, 'd8_advantage'),
            Die.predefined(self.sprites, 'd6_advantage'),
            Die.predefined(self.sprites, 'd4_advantage'),
            Die.predefined(self.sprites, 'd20_stone'),
            Die.predefined(self.sprites, 'd12_stone'),
            Die.predefined(self.sprites, 'd10_stone'),
            Die.predefined(self.sprites, 'd8_stone'),
            Die.predefined(self.sprites, 'd6_stone'),
            Die.predefined(self.sprites, 'd4_stone'),
            Die.predefined(self.sprites, 'd20_fire'),
            Die.predefined(self.sprites, 'd12_fire'),
            Die.predefined(self.sprites, 'd10_fire'),
            Die.predefined(self.sprites, 'd8_fire'),
            Die.predefined(self.sprites, 'd6_fire'),
            Die.predefined(self.sprites, 'd4_fire'),
            Die.predefined(self.sprites, 'd20_poison'),
            Die.predefined(self.sprites, 'd12_poison'),
            Die.predefined(self.sprites, 'd10_poison'),
            Die.predefined(self.sprites, 'd8_poison'),
            Die.predefined(self.sprites, 'd6_poison'),
            Die.predefined(self.sprites, 'd4_poison'),
            Die.predefined(self.sprites, 'd20_outlier'),
            Die.predefined(self.sprites, 'd12_outlier'),
            Die.predefined(self.sprites, 'd10_outlier'),
            Die.predefined(self.sprites, 'd8_outlier'),
            Die.predefined(self.sprites, 'd6_outlier'),
            Die.predefined(self.sprites, 'd4_outlier'),
            Die.predefined(self.sprites, 'd20_money'),
            Die.predefined(self.sprites, 'd12_money'),
            Die.predefined(self.sprites, 'd10_money'),
            Die.predefined(self.sprites, 'd8_money'),
            Die.predefined(self.sprites, 'd6_money'),
            Die.predefined(self.sprites, 'd4_money'),
        ], self.sprites['dice_bag'])

        player_attacks = [
            Attack([(3, 20)]),
            Attack([(1, 12)]),
            Attack([(2, 10)]),
            Attack([(2, 8)]),
            Attack([(6, 6)]),
        ]

        self.player = Actor(
            'player',
            self.sprites['art_boss'],
            self.sprites['dice_box_player'],
            player_dice_bag,
            player_attacks,
        )

        self.player_dice = []
        self.player_total = None

    def init_boss(self) -> None:
        boss_dice_bag = DiceBag([
            Die.predefined(self.sprites, 'd20_fluid'),
            Die.predefined(self.sprites, 'd12_fluid'),
            Die.predefined(self.sprites, 'd10_fluid'),
            Die.predefined(self.sprites, 'd8_fluid'),
            Die.predefined(self.sprites, 'd6_fluid'),
            Die.predefined(self.sprites, 'd4_fluid'),
            Die.predefined(self.sprites, 'd20_lucky'),
            Die.predefined(self.sprites, 'd12_lucky'),
            Die.predefined(self.sprites, 'd10_lucky'),
            Die.predefined(self.sprites, 'd8_lucky'),
            Die.predefined(self.sprites, 'd6_lucky'),
            Die.predefined(self.sprites, 'd4_lucky'),
            Die.predefined(self.sprites, 'd20_basic'),
            Die.predefined(self.sprites, 'd12_basic'),
            Die.predefined(self.sprites, 'd10_basic'),
            Die.predefined(self.sprites, 'd8_basic'),
            Die.predefined(self.sprites, 'd6_basic'),
            Die.predefined(self.sprites, 'd4_basic'),
            Die.predefined(self.sprites, 'd20_exploding'),
            Die.predefined(self.sprites, 'd12_exploding'),
            Die.predefined(self.sprites, 'd10_exploding'),
            Die.predefined(self.sprites, 'd8_exploding'),
            Die.predefined(self.sprites, 'd6_exploding'),
            Die.predefined(self.sprites, 'd4_exploding'),
            Die.predefined(self.sprites, 'd20_glass'),
            Die.predefined(self.sprites, 'd12_glass'),
            Die.predefined(self.sprites, 'd10_glass'),
            Die.predefined(self.sprites, 'd8_glass'),
            Die.predefined(self.sprites, 'd6_glass'),
            Die.predefined(self.sprites, 'd4_glass'),
            Die.predefined(self.sprites, 'd20_union'),
            Die.predefined(self.sprites, 'd12_union'),
            Die.predefined(self.sprites, 'd10_union'),
            Die.predefined(self.sprites, 'd8_union'),
            Die.predefined(self.sprites, 'd6_union'),
            Die.predefined(self.sprites, 'd4_union'),
            Die.predefined(self.sprites, 'd20_advantage'),
            Die.predefined(self.sprites, 'd12_advantage'),
            Die.predefined(self.sprites, 'd10_advantage'),
            Die.predefined(self.sprites, 'd8_advantage'),
            Die.predefined(self.sprites, 'd6_advantage'),
            Die.predefined(self.sprites, 'd4_advantage'),
            Die.predefined(self.sprites, 'd20_stone'),
            Die.predefined(self.sprites, 'd12_stone'),
            Die.predefined(self.sprites, 'd10_stone'),
            Die.predefined(self.sprites, 'd8_stone'),
            Die.predefined(self.sprites, 'd6_stone'),
            Die.predefined(self.sprites, 'd4_stone'),
            Die.predefined(self.sprites, 'd20_fire'),
            Die.predefined(self.sprites, 'd12_fire'),
            Die.predefined(self.sprites, 'd10_fire'),
            Die.predefined(self.sprites, 'd8_fire'),
            Die.predefined(self.sprites, 'd6_fire'),
            Die.predefined(self.sprites, 'd4_fire'),
            Die.predefined(self.sprites, 'd20_poison'),
            Die.predefined(self.sprites, 'd12_poison'),
            Die.predefined(self.sprites, 'd10_poison'),
            Die.predefined(self.sprites, 'd8_poison'),
            Die.predefined(self.sprites, 'd6_poison'),
            Die.predefined(self.sprites, 'd4_poison'),
            Die.predefined(self.sprites, 'd20_outlier'),
            Die.predefined(self.sprites, 'd12_outlier'),
            Die.predefined(self.sprites, 'd10_outlier'),
            Die.predefined(self.sprites, 'd8_outlier'),
            Die.predefined(self.sprites, 'd6_outlier'),
            Die.predefined(self.sprites, 'd4_outlier'),
            Die.predefined(self.sprites, 'd20_money'),
            Die.predefined(self.sprites, 'd12_money'),
            Die.predefined(self.sprites, 'd10_money'),
            Die.predefined(self.sprites, 'd8_money'),
            Die.predefined(self.sprites, 'd6_money'),
            Die.predefined(self.sprites, 'd4_money'),
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

        self.boss_dice = []
        self.boss_total = None

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

        label = str(self.boss_total) if self.boss_total is not None else ""
        self.boss.dice_box_art.draw(self.screen, (width * .2, 0), size = (width * .6, height * .375),
                            text=label)
        label = str(self.player_total) if self.player_total is not None else ""
        self.player.dice_box_art.draw(self.screen, (width * .2, height * .375), size = (width * .6, height * .375),
                                text=label)

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