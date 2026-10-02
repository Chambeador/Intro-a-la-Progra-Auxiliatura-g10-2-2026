def invertir(num):
    num_invertido = 0
    while num != 0:
        digito = num % 10
        num_invertido = num_invertido*10 + digito
        num = num//10
    return num_invertido