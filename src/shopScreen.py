import pygame
from screen import Screen
from button import Button
import random
from dice import Die
from diceCatalog import ALL_DICE_IDS, COMMON_DICE, UNCOMMON_DICE, RARE_DICE
from actors import Actor
import combatScreen


class shopScreen(Screen):
    def __init__(self, screen, width: int, height: int, sprites, player: Actor, level: int) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites
        self.level = level
        self.player = player
        self.player_dice = []

        self.items = []
        self.buttons = []

        self.player.money += 10

        self.init_shop_inventory()
        self.init_buttons()

    def init_shop_inventory(self):
        self.items = []
        
        slot1_common = random.choice(COMMON_DICE)
        slot2_commmon_uncommon = random.choice(COMMON_DICE + UNCOMMON_DICE)
        slot3_uncommon = random.choice(UNCOMMON_DICE)
        slot4_unccommon_rare = random.choice(UNCOMMON_DICE + RARE_DICE)
        slot5_random = random.choice(ALL_DICE_IDS)

        s1_die = Die.predefined(self.sprites, slot1_common)
        s2_die = Die.predefined(self.sprites, slot2_commmon_uncommon)
        s3_die = Die.predefined(self.sprites, slot3_uncommon)
        s4_die = Die.predefined(self.sprites, slot4_unccommon_rare)
        s5_die = Die.predefined(self.sprites, slot5_random)

        self.items.append({
            "die": s1_die,
            "cost": 2,
            "button": None,
            "sold": False
        })

        self.items.append({
            "die": s2_die,
            "cost": 2,
            "button": None,
            "sold": False
        })

        self.items.append({
            "die": s3_die,
            "cost": 3,
            "button": None,
            "sold": False
        })

        self.items.append({
            "die": s4_die,
            "cost": 4,
            "button": None,
            "sold": False
        })

        self.items.append({
            "die": s5_die,
            "cost": 5,
            "button": None,
            "sold": False
        })

    def init_buttons(self):
        self.buttons = []

        start_y = self.height * 0.2
        row_height = self.height * 0.1

        for i, item in enumerate(self.items):
            y = start_y + i * row_height

            button = Button(
                label = f"Buy ({item['cost']})",
                pos=(self.width * 0.6, y),
                size=(self.width * 0.3, row_height * 0.8),
                sprite=self.sprites['shopButton'],
                kind='buy',
                value=i
            )

            item['button'] = button 
            self.buttons.append(button)

        self.leave_button = Button(
            label="Leave",
            pos=(self.width * 0.75, self.height * 0.8),
            size=(self.width * 0.2, self.height * 0.15),
            sprite=self.sprites['button_toShop'],  # or a different sprite
            kind='leave',
        )

        self.buttons.append(self.leave_button)

    def draw(self) -> None:
        width, height = self.width, self.height

        self.sprites['background'].draw(self.screen, (0, 0), (width, height))

        ui_sections = [
            ((200, 150, 0), (width * .02, height * .8, width * .2, height * .2), f"Gold x{self.player.money}"),
            ((50, 50, 200), (width * .4, height * .8, width * .2, height * .1), "Re-Roll 1G"),
        ]

        font = pygame.font.SysFont(pygame.font.get_default_font(), 60)

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(self.screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            self.screen.blit(label, (w, h))

        start_y = self.height * 0.2
        row_height = self.height * 0.1

        for i, item in enumerate(self.items):
            y = start_y + i * row_height

            # draw the die icon
            item['die'].draw(self.screen, (self.width * 0.3, y), size=(50, 50))

            # cost text
            cost_text = font.render(f"{item['cost']}g", True, (255, 255, 255))
            self.screen.blit(cost_text, (self.width * 0.4, y))

            # buy button
            item['button'].draw(self.screen)

        # gold
        self.sprites['gold'].draw(self.screen,(width * .15, height * .8),size=(150, 150))

        # leave button
        self.leave_button.draw(self.screen)


    
    def on_event(self, event) -> Screen:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            for btn in self.buttons:
                if btn.inside(pos) and btn.kind == 'leave':
                    self.level += 1
                    self.player.money = 0
                    return combatScreen.combatScreen(self.screen, self.width, self.height, self.sprites, self.player, self.level)
                
                if btn.inside(pos) and btn.kind == 'buy':
                    # Check Money
                    # Subtract Money
                    # Add Die
                    # Make Item Unpurchaseable
                    index = btn.value
                    item = self.items[index]
                    cost = item['cost']

                    if item.get('sold'):
                        break

                    if self.player.money < cost:
                        print("Not enough gold!")
                        break
                    
                    self.player.money -= cost
                    self.player.dice_bag.add_dice([item['die']])
                    item['sold'] = True
                    item['button'].label = "Bought"
                    item['button'].kind = 'sold'
        return self