# https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2

from smbus2 import SMBus
import bme280


def pression():
    port = 1
    address = 0x77
    bus = SMBus(port)
    bme280.load_calibration_params(bus, address)
    bme280_data = bme280.sample(bus, address)
    return bme280_data.pressure
