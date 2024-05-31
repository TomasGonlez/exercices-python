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
    else:
        a= ''.join(a.split())
        for i in a:
            cont +=1
        return cont
a=lenght([100,20,30,40])
print(a)    