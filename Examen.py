
import math
def longitud(num: int):
    tamano = (int)(math.log10(num)+1)
    return tamano

def tiene_cero(num: int):
    respuesta = False
    while num > 0:
        digito = num%10
        if digito == 0:
            respuesta = True
        num = num //10
    return respuesta


def rotar(num: int):
    cant_digitos = longitud(num)
    potencia = 10**(cant_digitos-1)
    ultimos_d = num%potencia
    primer_d = num //potencia
    respuesta = ultimos_d*10+primer_d
    return respuesta



def rotar_cero(num: int, cant_digitos):
    potencia = 10**(cant_digitos-1)
    ultimos_d = num%potencia
    primer_d = num //potencia
    respuesta = ultimos_d*10+primer_d
    return respuesta


def calculo_f(num1: int, num2: int):
    #sabemos que ambos tiene la misma longitud
    suma = 0
    cnt = 0
    while num1 > 0:
        digito1 = num1%10
        digito2 = num2%20
        if digito1 == digito2:
            suma += digito1
            cnt += 1
        num1 = num1//10
        num2 = num2//10
    respuesta = suma*cnt
    return respuesta

def fortaleza(num1: int, num2: int):
    res = -1
    if longitud(num1) == longitud(num2):
        if tiene_cero(num1) or tiene_cero(num2):
            res = -1
        else:
            cant_digitos = longitud(num1)
            for i in range(cant_digitos-1):
                fortaleza = calculo_f(num1, num2)
                if fortaleza > res:
                    #encontre una mejor  respuesta
                    res = fortaleza
                num1 = rotar(num1)
            #se pued#en casar pq tiene misma longit
            #y no tienen al cero
    else:
        res = -1
    return res

def factorizacion(num: int):
    res = ""
    for div in range(2, num+1):
        if num%div == 0:
            contador = 0
            while num % div == 0:
                num = num //div
                contador += 1
            #tenemos al primo div
            #tenemos la cantd veces contador
            res = res + "*"+str(div)+"^"+str(contador)
    return res