def invertir(num):
    respuesta = ""
    num_invertido = 0
    copia_num = num
    while num != 0:
        digito = num % 10
        num_invertido = num_invertido*10 + digito
        num = num//10
    if num_invertido == copia_num:
        respuesta = "Si es capicua"
    else:
        respuesta = "No es capicua"
    return respuesta