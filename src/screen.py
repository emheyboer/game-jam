class Screen:
    def __init__(self, screen, width: int, height: int, sprites) -> None:
        pass

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