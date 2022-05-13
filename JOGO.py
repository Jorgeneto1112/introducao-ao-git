import random
from Sorteio_países import sorteia_pais 
from Base_países import normaliza
arquivo = open('DADOS.py', 'r')
texto=arquivo.read()
print(texto)
with open('DADOS.py') as arquivo:
    dados = normaliza(arquivo)

dados = normaliza(dados)    
sorteio =  sorteia_pais(dados)

print(sorteio)


print('Um país foi escolhido, tente adivinhar!\n')
pais = input('Qual o seu palpite?\n')

lista_paises = []
for pais in dados.keys():
    lista_paises.append(pais)

if pais in lista_paises:
    if pais == sorteio:
        print('Parabéns, você acertou!')
    else:
        print()
else:
    print('País desconhecido')