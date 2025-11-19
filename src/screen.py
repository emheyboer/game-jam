from sprites import Sprite
from actors import Actor

class Screen:
    def __init__(self, screen, width: int, height: int, sprites: dict[str, Sprite], player: Actor, level: int) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites
        self.player = player
        self.level = level

    def draw(self) -> None:
        """
        Renders the screen
        """
        pass
    
    def on_event(self, event):
        """
        Responds to an individual pygame event. On screen change, returns the new screen
        """
        return self