__author__ = "Mischa Jampen"

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from task.car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if type(gas_capacity) != float or type(gas_per_100km) != float or gas_capacity < 0 or gas_per_100km < 0:
            raise Warning("Invalid Input")

        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__available_gas = gas_capacity

    def fuel(self, f):
        self.__available_gas += f
        if self.__available_gas > self.__gas_capacity:
            raise Warning("Tank overflow")

    def get_gas_tank_status(self) -> tuple:
        tank_status = self.__available_gas
        gas_capacity = self.__gas_capacity
        return (tank_status, gas_capacity)

    def get_remaining_range(self):
        range_left = self.__available_gas / self.__gas_per_100km * 100
        return range_left

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input Type for distance")

        if self.get_remaining_range() < dist:
            self.__available_gas = 0
            raise Warning("Fuel is depleted!")

        else:
            self.__available_gas -= dist / 100 * self.__gas_per_100km
