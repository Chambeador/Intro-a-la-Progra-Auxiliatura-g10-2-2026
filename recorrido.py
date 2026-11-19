def recorrido_diagonal(mat: list[list[int]]) -> list[int]:
   n = len(mat) #cantidad de filas
   m = len(mat[0]) #cantidad de columnas
   fila = n-1 
   col = 0
   lista = []
   while col < m:
       #aqui estamos en el inciio de la diagonal
       fila_aux = fila
       col_aux = col
       while fila_aux < n and col_aux < m:
           lista.append(mat[fila_aux][col_aux])
           fila_aux +=1
           col_aux +=1
        #como sabemos el sig inicio de la sig diagonal
       if fila == 0:
          fila = 0
          col += 1
       else:
          fila -= 1
          col = 0
      
  return lista
       
def zigzag(mat):
    n = len(mat)
    m = len(mat[0])
    fila = 0
    col = 0
    subir = True
    lista = []
    for i in range(n+m-1):
        if subir == True:
            #tenemos que subir en la diagonal
            fila_aux = fila
            col_aux = col
            #subimos la diagonal
            while fila_aux >= 0 and col_aux < m:
                lista.append(mat[fila_aux][col_aux])
                fila_aux -= 1
                col_aux += 1
            #como sabemos el sig inicio
            if col_aux == m:
                col = m-1
                fila = fila_aux +2
            else:
                fila = fila_aux+1
                col = col_aux
            subir = not(subir)
        else:
            #subir es false debemos de bajar
            #en la diagonal
            fila_aux = fila
            col_aux = col
            while fila_aux < n and col_aux >= 0:
                lista.append(mat[fila_aux][col_aux])
                fila_aux += 1
                col_aux -=1            
            #encontrar el sig inicio
            if fila_aux == n:
                fila = n-1
                col = col_aux+2
            else:
                fila = fila_aux
                col = col_aux+1
            subir = not(subir)
    return lista
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
