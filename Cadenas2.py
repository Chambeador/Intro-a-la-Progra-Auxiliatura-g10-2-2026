def secuencia(k: int) -> str:
    ini = ord("a")
    respuesta = ""
    for i in range(k):
        respuesta = respuesta + chr(ini+i)+" "
    return respuesta


def aparece(cad: str, posC: int, pat: str) -> bool:
    posP = 0
    aparece_patron = True
    while posC < len(cad) and posP < len(pat):
        if cad[posC] != pat[posP]:
            #vacio no hacemos
            #vamos todo bien
            aparece_patron = False
        posC += 1
        posP += 1
    return aparece_patron



def contar_ocurrencias(cad: str, pat: str) -> int:
    #cantidad de veces que aparece
    #el pat dentro de cad
    cantidad_oc = 0
    for pos in range(len(cad)-len(pat)+1):
        if cad[pos] == pat[0]:
            #la primera letra del pat
            #coincidio con la letra de la cadena
            if aparece(cad, pos, pat):
                #Programa aparece lo que hace es
                #verificar si el pat aparece en
                #la posicion pos de la cad
                cantidad_oc +=1
    return cantidad_oc