def paridad(num: int) -> str:
    respuesta = ""
    if num%2 == 0:
        respuesta = "Par"
    else: 
        respuesta = "Impar"
    return respuesta