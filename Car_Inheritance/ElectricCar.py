#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km) -> float:
        if type(battery_size) != float or type(battery_range_km) != float or battery_size < 0 or battery_range_km < 0:
            raise Warning("Invalid Input")

        self.battery_size = battery_size
        self.battery_range_km = battery_range_km
        self.charge_left = battery_size

    def charge(self, kwh) -> float:
        if type(kwh) != float or kwh < 0:
            raise Warning("Invalid Input")
        if self.charge_left + kwh > self.battery_size:
            self.charge_left = self.battery_size
            raise Warning("battery overcharged")
        else:
            self.charge_left += kwh

    def get_battery_status(self) -> tuple:
        battery_status = self.charge_left
        battery_size = self.battery_size
        return (battery_status, battery_size)

    def get_remaining_range(self) -> float:
        range_left = self.charge_left/self.battery_size * self.battery_range_km
        return range_left

    def drive(self, dist) -> float:
        if dist < 0 or type(dist) != float:
            raise Warning("Invalid Input")
            
        if self.get_remaining_range() < dist:
            self.charge_left = 0
            raise Warning("Battery empty")
        else:
            self.charge_left -= dist * self.battery_size / self.battery_range_km
        