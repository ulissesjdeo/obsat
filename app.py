from os.path import getctime, exists
from calendar import timegm
from requests import post
from time import gmtime
from os import makedirs
from glob import glob


if not exists('debug.lock'):
    DEBUG = False
    from modules import battery, position, json, image, bme
    from subprocess import run
else:
    DEBUG = True
    from modules import json, image

try: makedirs('data')
except FileExistsError: pass

try: makedirs('photos')
except FileExistsError: pass

timestamp = timegm(gmtime())

if not DEBUG:
    battery = battery.level()
    position = position.data()
    file = f"photos/{timestamp}.jpg"
    run(f"cd obsat && libcamera-jpeg -o {file} --nopreview --timeout 5000")
    temperature = bme.temperature()
    pressure = bme.pressure()
    url = open('other/address.cfg', 'r').read()
else:
    battery = 95
    position = {"g": [-0.298, -0.298, -0.298], "a": [-0.298, -0.298, -0.298]}
    file = 'other/debug.jpg'
    temperature = 51.32751778398884
    pressure = 1014.824777283405
    url = 'https://obsat.org.br/teste_post/envio.php'  # https://obsat.org.br/teste_post/index.php

people = image.analyze(file, timestamp)

with open(f'data/{timestamp}.json', 'w') as data:
    data.write(json.finalize(battery, temperature, position, people, pressure, debug=DEBUG))
    data.close()

latest = max(glob('data/*'), key=getctime)
with open(latest, 'r') as latest:
    content = latest.read()
    latest.close()
request = post(url, data=content)

if DEBUG: print(content)
