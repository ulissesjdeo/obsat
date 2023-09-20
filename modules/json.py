def finalize(battery, temperature, position, people):
    return '{' + f'"b":{battery},"t":{temperature},"g":"{position["g"][0]},{position["g"][1]},{position["g"][2]}","a":"{position["a"][0]},{position["a"][1]},{position["a"][2]}","n":{people}' + '}'
