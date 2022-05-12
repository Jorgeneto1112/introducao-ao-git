def normaliza(dicio):
    saida = {}

    for cont in dicio:
        for pais, info in dicio[cont].items():
            saida[pais] = info

    return saida