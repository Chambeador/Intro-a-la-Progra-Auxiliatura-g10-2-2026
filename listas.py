def reduccir(cad : str) -> str:
    reducido = ""
    cantidad = 0
    letra_anterior = cad[0]
    for i in range(len(cad)):
        if letra_anterior == cad[i]:
            #si son iguales hacemos algo
            cantidad += 1
        else:
            #no son iguales
            #meter a la respuesta
            nuevo_termino = str(cantidad)+letra_anterior 
            reducido = reducido + nuevo_termino
            #resetear los valores
            cantidad = 1
            letra_anterior = cad[i]
    reducido = reducido + str(cantidad)+letra_anterior
    return reducido







def suma_lista(lista: list[int]) -> int:
    suma_elementos = 0
    for i in range(len(lista)):
        suma_elementos += lista[i]
    return suma_elementos


def aparece_lista(lista: list[int], x: int) -> bool:
    aparece = False
    for i in range(len(lista)):
        if x == lista[i]:
            aparece = True
    return aparece




   #la lista tiene tamano n-1 y no hay repetidos
   # y la lista solo contiene numeros del 1 al n
def encontrar_perdido(n: int, lista: list[int]) -> int:
    perdido = 1
    buscado = 1
    while buscado <= n:
        if aparece_lista(lista, buscado):
            buscado += 1
        else:
            perdido = buscado
            buscado = n+1
    return perdido
    
    






def esta_ordenada(lista: list[int]) -> bool:
    #True si esta ordenada
    #Falso si no esta ordenada
    ordenada = True
    for i in range(1, len(lista)):
        if lista[i-1] > lista[i]:
            #todo esta okey
            ordenada = False
    return ordenada





