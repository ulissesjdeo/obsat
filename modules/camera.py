# https://www.electronicwings.com/raspberry-pi/pi-camera-module-interface-with-raspberry-pi-using-python

from picamera import PiCamera
from time import sleep


def capture(timestamp):
    file = f'photos/{timestamp}.jpeg'

    cam = PiCamera()
    cam.resolution = (1024, 768)
    cam.brightness = 60

    cama.start_preview()
    sleep(5)
    cam.capture(file)
    cam.stop_preview()
    return file
