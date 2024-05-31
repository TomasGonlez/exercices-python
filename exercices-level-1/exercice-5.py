'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''
def sum(lista):
    suma = 0
    tipo = type(lista)
    if tipo is list:
        for i in lista:
            suma +=i
        return suma
    else:
        return "Error, no es una lista"

def multip(lista):
    factorial = 1
    tipo = type(lista)
    if tipo is list:
        for i in lista:
            factorial *= i
        return factorial
    else:
        return "Error, no es una lista"

s = sum([4,5,6,7])
m = multip([4,5,6,7])
print(s,m)