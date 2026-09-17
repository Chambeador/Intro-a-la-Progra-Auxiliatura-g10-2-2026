def clasificador(l1: int, l2: int, l3: int) -> str:
    respuesta = ""
    if l1+l2 >= l3 and l1+l3 >= l2 and l2+l3 >= l1:
        if l1 == l2 == l3:
            respuesta = "Equilatero"
        elif l1 == l2 or l1 == l3 or l2 == l3:
            respuesta = "Isoceles"
        else :
            respuesta = "Escaleno"
    else:
        respuesta = "No es un triangulo"

    return respuesta