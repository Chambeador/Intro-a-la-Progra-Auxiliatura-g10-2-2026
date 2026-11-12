def suma_matriz(mat):
    suma = 0
    cant_filas = len(mat);
    cant_columnas = len(mat[0])
    for fila in range(cant_filas):
        for col in range(cant_columnas):
            suma += mat[fila][col]
    return suma
    
    
def recorrido_raro(mat):
    lista = []
    colI = 0
    colF = len(mat[0])-1
    cant_filas = len(mat)
    while colI <= colF:
        #utilizar un bucle for para iterar las filas
        #ya que la columna estafija
        for fila in range(cant_filas):
            lista.append(mat[fila][colI])
        #hacer lo mismo pero para la columna final
        if colI != colF: 
            for fila in range(cant_filas):
                lista.append(mat[fila][colF])
            #actualizar las flechitas
        colI += 1
        colF -= 1
    
    return lista


def contar(valor, lista):
    contador = 0
    for i in range(len(lista)):
        if valor == lista[i]:
            contador += 1
    return contador

def frecuencia(lista):
    mejor_elemento = -1
    cantidad = -1
    for i in range(len(lista)):
        elemento = lista[i]
        if contar(elemento, lista) > cantidad:
            cantidad = contar(elemento, lista)
            mejor_elemento = elemento
    return mejor_elemento
    
    









    
    
    
