def x(n):
    '''Funcion que calcula el factorial de un numero'''
    

    if n == 0:
        return 1
    else:
        return n * x(n - 1)
    
n = int(input("introduzca un numero entero"))
print(x(n))
