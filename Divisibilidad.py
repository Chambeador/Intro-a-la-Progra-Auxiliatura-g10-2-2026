def divisibilidad(num: int) -> bool:
    respuesta = False
    num_c = num
    suma = 0
    suma = suma + num%10
    num = num //10
    suma = suma + num%10
    num = num //10
    suma = suma + num%10
    num = num //10
    if num_c % suma == 0:
        respuesta = True
    return respuesta