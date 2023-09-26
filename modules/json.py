def finalize(battery, temperature, position, people, pression):
    return ('{\n' +
            f'  "equipe": "scottinik",\n'
            f'  "bateria": {battery},\n'
            f'  "temperatura": {temperature},\n'
            f'  "pressao": {pression},\n'
            '  "giroscopio": {\n    "x": ' + f'{position["g"][0]}' + ',\n    "y": ' + f'{position["g"][1]}' + ',\n    "z": ' + f'{position["g"][2]}' + '\n  },\n'
            '  "acelerometro": {\n    "x": ' + f'{position["a"][0]}' + ',\n    "y": ' + f'{position["a"][1]}' + ',\n    "z": ' + f'{position["a"][2]}' + '\n  },\n'
            '  "payload": {\n' + '    "n": ' + f'{people}' + '\n  }\n'
            + '}')
