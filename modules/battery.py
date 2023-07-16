from machine import Pin, ADC
from time import sleep


def level():
    potentiometer = ADC(28)
    potentiometer_value = potentiometer.read_u16()
    print(potentiometer_value)
    sleep(0.25)
