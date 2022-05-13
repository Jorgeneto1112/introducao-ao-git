from DADOS import *
from Sorteio_países import sorteia_pais 
from Base_países import normaliza

dados = normaliza(dados)

sorteio =  sorteia_pais(dados)

print(sorteio)