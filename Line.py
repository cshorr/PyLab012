from Point import Point

class Line:
    """Represents a line segment defined by two points."""
    def __init__(self, p1:Point, p2:Point):
        self._p1 = p1
        self._p2 = p2

    def translate(self, dx, dy, end: int):

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'

def main():
    l = Line(Point(5, 5), Point(3, 3))
    print(l.getPoint(end=2).translate(1, 1))

    if __name__ == '__main__':
        main()