# https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2

from smbus2 import SMBus
import bme280 as bme

address = 0x77  # Adafruit BME280 address. Other BME280s may be different
bus = SMBus(1)


def data():
    bme.load_calibration_params(bus, address)
    return bme.sample(bus, address)


def pressure(): return data().pressure
def temperature(): return data().temperature
