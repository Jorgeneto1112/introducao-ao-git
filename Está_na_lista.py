def esta_na_lista(pais,lista_paises):
    lista_apenas_pais=[]
    for pais_distancia in lista_paises:
        lista_apenas_pais.append(pais_distancia[0])
    if pais in lista_apenas_pais:
        return True 
    elif pais not in lista_apenas_pais:
        return False
        
        