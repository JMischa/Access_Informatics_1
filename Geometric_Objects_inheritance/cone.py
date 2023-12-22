__author__ = "Mischa Jampen"
from math import pi


class Cone(GeometricObject):
    def __init__(self, color, filled, radius, vertical_height, slant_height):
        super().__init__(color, filled)
        self.radius = radius
        self.vertical_height = vertical_height
        self. slant_height = slant_height

    def area(self):
        return round(pi * self.radius ** 2 + 2 * pi * self.radius * self.slant_height,2)

    def volume(self):
        return round((1/3) * pi * self.radius ** 2 * self.vertical_height,2)
