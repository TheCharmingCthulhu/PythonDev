import math

class Shape():
    def __init__(self):
        pass

    def GetArea(self):
        return None;

    def GetPerimeter(self):
        return None;

class Rect(Shape):
    def __init__(self, a, b):
        Shape.__init__(self);

        self.a = a;
        self.b = b;

    def GetArea(self):
        return self.a * self.b;

    def GetPerimeter(self):
        return (a * 2) + (b * 2);

class Triangle(Shape):
    def __init__(self, *sides):
        Shape.__init__(self);

        if len(sides) >= 2:
            self.sides = sides;

    def GetArea(self, height):
        if height != 0 and len(self.sides) > 0:
            return (self.sides[0] * height) / 2

    def GetPerimeter(self):
        return a + b + c;

class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self);

        self.r = radius;

    def GetArea(self):
        return math.pi * math.pow(r, 2);

    def GetPerimeter(self):
        return math.pi * r * 2;

    def GetDiameter(self):
        return r * 2;


