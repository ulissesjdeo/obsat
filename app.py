from calendar import timegm
from os.path import exists
from time import gmtime

if not exists('debug.lock'):
    DEBUG = False
else:
    DEBUG = True

if not DEBUG:
    from modules import battery, temperature, position, camera, json, image
else:
    from modules import json, image

if __name__ == '__main__':
    timestamp = timegm(gmtime())
    if not DEBUG:
        battery = battery.level()
        temperature = temperature.data()
        position = position.data()
        file = camera.capture(timestamp)
    else:
        battery = 95
        temperature = 25
        position = {"g": [-0.298, -0.298, -0.298], "a": [-0.298, -0.298, -0.298]}
        file = 'debug.jpg'

    people = image.analyze(file, timestamp)

    with open(f'data/{timestamp}.json', 'w') as data:
        data.write(json.finalize(battery, temperature, position, people))
        data.close()
