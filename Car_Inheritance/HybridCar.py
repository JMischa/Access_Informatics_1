__author__ = "Mischa Jampen"
from CombustionCar import CombustionCar
from ElectricCar import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km) -> float:
        CombustionCar.__init__(gas_per_100km, gas_capacity)
        ElectricCar.__init__(battery_size, battery_range_km)
        self.COMBUSTION = 0
        self.ELECTRIC = 1
        self.mode = self.ELECTRIC

    def switch_to_combustion(self):
        self.mode = self.COMBUSTION

    def switch_to_electric(self):
        self.mode = self.ELECTRIC

    def get_remaining_range(self):
        return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, float):
            raise Warning
        if dist < 0:
            raise Warning
        c_range = CombustionCar.get_remaining_range(self)
        e_range = ElectricCar.get_remaining_range(self)
        if dist > self.get_remaining_range():
            CombustionCar.drive(self,c_range)
            ElectricCar.drive(self,e_range)
            raise Warning('both modes depleted')
        if self.mode == 0:
            if c_range <= dist:
                CombustionCar.drive(self, c_range)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - c_range)
            else: CombustionCar.drive(self, dist)
        elif self.mode == 1:
            if e_range <= dist:
                ElectricCar.drive(self, e_range)
                self.switch_to_combustion
                CombustionCar.drive(self, dist - e_range)
            else: ElectricCar.drive(self, dist)


