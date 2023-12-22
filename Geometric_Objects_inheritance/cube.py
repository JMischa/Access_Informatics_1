__author__ = "Mischa Jampen"



class Cube(GeometricObject):
    def __init__(self, color, filled, side_length):
        super().__init__(color,filled)
        self.side_length = side_length

    def area(self):
        return round(6 * (self.side_length ** 2),2)

    def volume(self):
        return round(self.side_length ** 3,2)
