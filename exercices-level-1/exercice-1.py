'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''


def max(a,b):
    if a < b:
        return b
    if b < a:
        return a
print(max(100,101))


