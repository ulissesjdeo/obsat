def finalize(battery, temperature, position, people, pression):
    return ('{\n' +
            f'  "equipe": "scottinik",\n'
            f'  "bateria": {battery},\n'
            f'  "temperatura": {temperature},\n'
            f'  "pressao": {pression},\n'
            f'  "giroscopio": [{position["g"][0]}, {position["g"][1]}, {position["g"][2]}],\n'
            f'  "acelerometro": [{position["a"][0]}, {position["a"][1]}, {position["a"][2]}],\n'
            '  "payload": {\n' + '    "n": ' + f'{people}' + '\n  }\n'
            + '}')
