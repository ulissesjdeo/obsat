from requests import post
from sys import argv


filename = argv[1]
content = open(filename, 'r').read()

request = post(open('address.config', 'r').read(), json=content)
