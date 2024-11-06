#tres numeros enteros
#ordenar de mayor a menor e imprimir

a = int(input("Digite el numero 1: "))
b = int(input("Digite el numero 2: "))
c = int(input("Digite el numero 3: "))

#ordenar de mayor a menor

if a > b and a > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)

elif b > a and b > c:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a > b:
        print (c, a, b)
    else:
        print (c, b, a)
