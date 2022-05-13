from Sorteio_países import sorteia_pais 
from Base_países import normaliza

with open('DADOS.py') as arquivo:
    dados = normaliza(arquivo)

sorteio =  sorteia_pais(dados)

print(sorteio)