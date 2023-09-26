from os.path import exists
from requests import post
from sys import argv

if not exists('debug.lock'): url = open('config/address.cfg', 'r').read()
else: url = 'https://obsat.org.br/teste_post/envio.php'  # https://obsat.org.br/teste_post/index.php

filename = argv[1]
content = open(filename, 'r').read()
request = post(url, json=content)

if exists('debug.lock'): print(content)
