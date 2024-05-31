'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def verifChar(char):
    vocales = ['a','e','i','o','u']
    if char in vocales:
        return True
    else:
        return False
x = verifChar('a')
print(x)