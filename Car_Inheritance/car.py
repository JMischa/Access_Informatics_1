__author__ = "Mischa Jampen"

class Car(ABC):

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod
    def drive(self, dist):
        pass