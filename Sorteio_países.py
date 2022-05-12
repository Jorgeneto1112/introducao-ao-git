import random
def sorteia_pais(dicio):
    lista = []

    for pais in dicio.keys():
        lista.append(pais)

    sorteio = random.choice(lista)

    return sorteio