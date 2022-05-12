def adiciona_em_ordem(pais,distancia_do_pais,lista):
    nova_lista=[]
    lista_nomes=[]
    lista_distancias=[]
    lista_distancias=[]
    adicionar=[pais,distancia_do_pais]
    if lista == nova_lista:
        lista.append(adicionar)
        return lista

    for paises in lista:
        lista_nomes.append(paises[0])
        lista_distancias.append(paises[1])
    if pais in lista_nomes:
        return lista


    if pais not in lista_nomes:
        for paises in lista:
            distancia=paises[1]
            if distancia_do_pais>distancia:
                nova_lista.append(paises)
            elif adicionar in nova_lista:
                nova_lista.append(paises)
            elif distancia_do_pais<distancia:
                nova_lista.append(adicionar)
                nova_lista.append(paises)
        if adicionar not in nova_lista:
            nova_lista.append(adicionar)
        return nova_lista
print(adiciona_em_ordem('japao',13836, [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['siria', 5919],
    ['india', 9919]]))
            

            
           
        
   
        
            
        