def serie(x):
    cantidad = 0
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = x*3+1
        cantidad+=1
    return cantidad