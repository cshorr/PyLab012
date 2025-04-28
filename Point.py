class Point:
    """Represents a point in 2D space."""
    def __init__(self, x: int, y : int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        return self
