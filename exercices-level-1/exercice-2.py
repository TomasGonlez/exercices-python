'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def max_3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:               
        return c  
x = max_3(520,643,245)
print(x)



