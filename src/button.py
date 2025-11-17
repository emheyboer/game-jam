from sprites import Sprite


class Button:
    def __init__(self, label: str, pos: tuple[float, float], size: tuple[float, float], sprite: Sprite) -> None:
        self.pos = pos
        self.size = size
        
        self.sprite = sprite
        self.label = label

    def inside(self, pos: tuple[float, float]) -> bool:
        x, y = pos
        minX, minY = self.pos
        deltaX, deltaY = self.size
        maxX, maxY = minX + deltaX, minY + deltaY
        return minX <= x <= maxX and minY <= y <= maxY
    
    def draw(self, screen) -> None:
        self.sprite.draw(screen, self.pos, scale=self.size, text=self.label)