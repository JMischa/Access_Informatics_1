__author__ = "Mischa Jampen"


class GeometricObject(ABC):

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass
