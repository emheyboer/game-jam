class Screen:
    def __init__(self, screen, width: int, height: int, sprites) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.sprites = sprites

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