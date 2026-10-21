def caracter_posicion(cadena:str, posicion: int) -> str:
    letra = cadena[posicion]
    return letra

def contar_vocales(palabra: str) -> int:
    cantidad_vocales = 0
    for pos in range(len(palabra)):
        caracter = palabra[pos]
        if caracter in "aeiou":
            #si entra al if sabemos que es una
            #vocal
            cantidad_vocales += 1
        
    return cantidad_vocales


def es_palindroma(cadena: str) -> bool:
    izq = 0
    der = len(cadena)-1
    es_pal = True
    while izq <= der:
        if cadena[izq] != cadena[der]:
            es_pal = False        
        izq += 1
        der -= 1
    return es_pal


