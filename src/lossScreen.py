import pygame
from screen import Screen


class lossScreen(Screen):
    def __init__(self, screen, width: int, height: int, sprites) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites
        lossScreen.draw(self)

    def draw(self) -> None:
        print("Drawin")
        width, height = self.width, self.height
        self.sprites['background_Loss'].draw(self.screen,(0, 0),size=(width, height))

    def on_event(self, event) -> Screen:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return "retry"
    
        return self

    