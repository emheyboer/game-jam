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
    def __init__(self, screen, width: int, height: int, sprites: dict[str, Sprite], player: Actor, level: int) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites
        self.level = level

        self.player = player
        self.player_dice = []
        self.player_total = None
        
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

    def init_boss(self) -> None:
        self.boss = load_boss(self.sprites, self.level)
        self.boss_dice = []
        self.boss_total = None

    def draw(self) -> None:
        width, height = self.width, self.height

        self.sprites['background'].draw(self.screen, (0, 0), (width, height))

        label = str(self.boss_total) if self.boss_total is not None else ""
        self.boss.dice_box_art.draw(self.screen, (width * .2, 0), size = (width * .6, height * .375),
                            text=label)
        label = str(self.player_total) if self.player_total is not None else ""
        self.player.dice_box_art.draw(self.screen, (width * .2, height * .375), size = (width * .6, height * .375),
                                text=label)


        # self.boss.dice_bag.draw(self.screen, (width * .8, height * .475), size = (width * .225, height * .225))
        # self.player.dice_bag.draw(self.screen, (width * .8, height * .1), size = (width * .225, height * .225))

        self.boss.profile_art.draw(self.screen, (0, height * 0), size = (width * .225, width * .225))

        for btn in self.buttons:
            btn.draw(self.screen)

        self.draw_dice_in_box('boss', self.boss_dice)
        self.draw_dice_in_box('player', self.player_dice)

        self.draw_dice_in_bag()


    def draw_dice_in_box(self, box: str, dice: list[Die]) -> None:
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

    def draw_dice_in_bag(self) -> None:
        width, height = self.width, self.height
        dice = self.player.dice_bag.all_dice()
        y = height * .45

        deltaX = width * .04
        size = (deltaX, deltaX)
        deltaY = -height * .02
        lineOffset = height * .104
        # # adapt sizes & positions to fit in the same space
        #     divisor = count / 12
        #     deltaX = width * .04 / divisor
        #     size = (deltaX, deltaX)
        #     deltaY = -height * .02 / divisor
        #     lineOffset = height * .104 / divisor

        x = width * 0
        for die in dice:
            y += deltaY
            if x + deltaX > width * .2:
                y += lineOffset
                x = 0
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
                    return shopScreen(self.screen, self.width, self.height, self.sprites, self.player, self.level)                

        return self
    


def load_boss(sprites: dict[str, Sprite], index: int) -> Actor:
    bosses = [
        Actor(
            'vesphira',
            sprites['vesphira'],
            sprites['dice_box_boss'],
            DiceBag([
                Die.predefined(sprites, 'd8_advantage'),
                Die.predefined(sprites, 'd8_advantage'),
                Die.predefined(sprites, 'd8_outlier'),
                Die.predefined(sprites, 'd8_outlier'),
                    ], sprites['dice_bag']),
            [
                Attack([(2, 8)]),
                Attack([(3, 8)]),
            ],
        ),
        Actor(
            'tootle',
            sprites['tootle'],
            sprites['dice_box_boss'],
            DiceBag([
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd4_union'),
                Die.predefined(sprites, 'd6_basic'),
                Die.predefined(sprites, 'd6_basic'),
                Die.predefined(sprites, 'd6_basic'),
                Die.predefined(sprites, 'd6_basic'),
                Die.predefined(sprites, 'd6_basic'),
                Die.predefined(sprites, 'd6_basic'),
                    ], sprites['dice_bag']),
            [
                Attack([(6, 4)]),
                Attack([(1,4), (1, 6)]),
            ],
        ),
        Actor(
            'vesphira',
            sprites['vesphira'],
            sprites['dice_box_boss'],
            DiceBag([
                    ], sprites['dice_bag']),
            [
                Attack([(2, 8), (3, 6)]),
                Attack([(3, 20)]),
            ],
        ),
        Actor(
            'dice goblin',
            sprites['dice_goblin'],
            sprites['dice_box_boss'],
            DiceBag([
                    ], sprites['dice_bag']),
            [
                Attack([(2, 8), (3, 6)]),
                Attack([(3, 20)]),
            ],
        )
    ]
    return bosses[index]