from lib.car import Car
from lib.vehicle import Vehicle

def test_is_subclass():
    assert issubclass(Car, Vehicle)