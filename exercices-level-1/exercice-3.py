'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def lenght(a):
    cont = 0
    t=type(a)
    if t is list:
        for i in a:
            cont +=1
        return cont
    a= ''.join(a.split())
    for i in a:
        cont +=1
    return cont
a=lenght("[1,2,3,4,5,6,7,8,9,10,11,12,13]")
print(a)