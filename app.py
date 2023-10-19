from os.path import getctime, exists
from modules import json, image
from calendar import timegm
from requests import post
from time import gmtime
from os import makedirs
from glob import glob

timestamp = timegm(gmtime())

if not exists('debug.lock'):
    DEBUG = False
    debuging = []
else:
    with open('debug.lock', 'r') as debuging:
        debuging = debuging.read().split(',')
    DEBUG = True

try: makedirs('data')
except FileExistsError: pass

try: makedirs('photos')
except FileExistsError: pass

if 'battery' in debuging:
    battery = 95
else:
    from modules import battery
    battery = battery.level()

if 'position' in debuging:
    position = {"g": [-0.298, -0.298, -0.298], "a": [-0.298, -0.298, -0.298]}
else:
    from modules import position
    position = position.data()

if 'camera' in debuging:
    file = 'other/debug.jpg'
else:
    from subprocess import run
    file = f"photos/{timestamp}.jpg"
    run(f"cd obsat && libcamera-jpeg -o {file} --nopreview --timeout 5000")

if 'temperature' in debuging:
    temperature = 51.32751778398884
else:
    from modules import bme
    temperature = bme.temperature()

if 'pressure' in debuging:
    pressure = 1014.824777283405
else:
    from modules import bme
    pressure = bme.pressure()

if 'url' in debuging:
    url = 'https://obsat.org.br/teste_post/envio.php'  # https://obsat.org.br/teste_post/index.php
else:
    url = open('other/address.cfg', 'r').read()

people = image.analyze(file, timestamp)

with open(f'data/{timestamp}.json', 'w') as data:
    data.write(json.finalize(battery, temperature, position, people, pressure, debug=DEBUG))
    data.close()

with open(max(glob('data/*'), key=getctime), 'r') as latest:
    content = latest.read()
    latest.close()

request = post(url, data=content)
if DEBUG: print(content)
