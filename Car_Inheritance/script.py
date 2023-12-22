__author__ = "Mischa Jampen"

from CombustionCar import CombustionCar
from ElectricCar import ElectricCar
from HybridCar import HybridCar


c = CombustionCar(40.0, 8.0)
print(c.get_remaining_range()) # 500
c.drive(25.0)
print(c.get_gas_tank_status()) # (38.0, 40.0)
try:
    c.drive(1000.0)
except Warning:
    print("fuel is depleted")
else:
    raise Warning("Here should have been raised a warning!")

e = ElectricCar(25.0, 500.0)
e.drive(100.0)
e.charge(2.0)
print(e.get_battery_status()) # (22.0, 25)

h = HybridCar(40.0, 8.0, 30.0, 300.0)
h.switch_to_combustion()
print(h.drive(600.0)) # depletes fuel, auto-switch
print(h.get_gas_tank_status()) # (0.0, 40.0)
print(h.get_battery_status()) # (20.0, 25.0) 