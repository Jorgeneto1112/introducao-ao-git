import random 
def sorteia_letra(palavra,lista_letras_restritas):
    alfabeto=['A','a','B', 'b', 'C','c', 'D','d', 'E','e', 'F','f', 'G','g', 'H','h', 'I','i', 'J','j', 'K','k', 'L','l', 'M','m', 'N','n', 'O','o', 'P','p', 'Q','q', 'R','r', 'S','s', 'T','t', 'U','u', 'V','v', 'W','w', 'X','x', 'Y','y', 'Z','z']
    string_vazia=''
    lista_letras_semcaractere=[]
    lista_para_sorteio=[]
    lista_vazia=[]
    lista_maiuscula=[]
    for letra in lista_letras_restritas:
        letra_maiuscula=letra.upper()
        lista_maiuscula.append(letra_maiuscula)
    if palavra == string_vazia:
        return ''
    for letra in palavra:
        if letra in alfabeto:
            lista_letras_semcaractere.append(letra)
    
    for quase_permitido in lista_letras_semcaractere:
        if quase_permitido not in lista_letras_restritas and quase_permitido not in lista_maiuscula:
            lista_para_sorteio.append(quase_permitido)
    
    if lista_para_sorteio == lista_vazia:
        return ''
    
    else:
        return random.choice(lista_para_sorteio)
print(sorteia_letra('Andorra a-Velha',['a', 'r']))


        
        


    
    