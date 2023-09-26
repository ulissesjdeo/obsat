from calendar import timegm
from os.path import exists
from time import gmtime
from os import makedirs


if not exists('debug.lock'):
    DEBUG = False
    from modules import battery, temperature, position, camera, json, image, pression
else:
    DEBUG = True
    from modules import json, image

try:
    makedirs('data')
except FileExistsError:
    pass

try:
    makedirs('photos')
except FileExistsError:
    pass

timestamp = timegm(gmtime())

if not DEBUG:
    battery = battery.level()
    temperature = temperature.data()
    position = position.data()
    file = camera.capture(timestamp)
    pression = pression.pression()
else:
    battery = 95
    temperature = -220
    position = {"g": [-0.298, -0.298, -0.298], "a": [-0.298, -0.298, -0.298]}
    file = 'other/debug.jpg'
    pression = 1014.824777283405

people = image.analyze(file, timestamp)

with open(f'data/{timestamp}.json', 'w') as data:
    data.write(json.finalize(battery, temperature, position, people, pression))
    data.close()
