import pygame
from screen import Screen


# TO-DO
#  - Generate Random Shop items based off of rarity
#  - Reroll button
#  -

class shopScreen(Screen):
    def __init__(self, screen, width: int, height: int, sprites) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites

    def draw(self) -> None:
        width, height = self.width, self.height

        ui_sections = [
            ((200, 0, 0), (width * .15, height * .1, width * .2, height * .2), "Item 1"),
            ((200, 0, 0), (width * .4, height * .1, width * .2, height * .2), "Item 2"),
            ((200, 0, 0), (width * .65, height * .1, width * .2, height * .2), "Item 3"),

            ((200, 0, 0), (width * .25, height * .4, width * .2, height * .2), "Item 4"),
            ((200, 0, 0), (width * .55, height * .4, width * .2, height * .2), "Item 5"),

            ((200, 150, 0), (width * .02, height * .8, width * .2, height * .2), "Gold"),
            ((50, 50, 200), (width * .4, height * .8, width * .2, height * .1), "Re-Roll 1G"),
            ((0, 200, 200), (width * .75, height * .8, width * .2, height * .2), "Leave"),
        ]

        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

        for section in ui_sections:
            color, rect, text = section

            pygame.draw.rect(self.screen, color, rect)

            label = font.render(text, False, (255, 255, 255))

            w, h, _, _ = rect
            self.screen.blit(label, (w, h))


    
    def on_event(self, event) -> Screen:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

        return self