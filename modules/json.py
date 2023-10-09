def finalize(battery, temperature, position, people, pression, debug=True):
    if debug:
        return ('{\n' +
                f'  "equipe": "sctk",\n'
                f'  "bateria": {battery},\n'
                f'  "temperatura": {temperature},\n'
                f'  "pressao": {pression},\n'
                f'  "giroscopio": [{position["g"][0]}, {position["g"][1]}, {position["g"][2]}],\n'
                f'  "acelerometro": [{position["a"][0]}, {position["a"][1]}, {position["a"][2]}],\n'
                '  "payload": {\n' + '    "n": ' + f'{people}' + '\n  }\n'
                + '}')
    else:
        return ('{' +
                f'"equipe":"sctk","bateria":{battery},"temperatura":{temperature},"pressao":{pression},"giroscopio":[{position["g"][0]},{position["g"][1]},{position["g"][2]}],"acelerometro":[{position["a"][0]},{position["a"][1]},{position["a"][2]}],' + '"payload":{"n":' + f'{people}' + '}}')
