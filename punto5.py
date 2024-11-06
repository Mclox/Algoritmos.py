#capturar 3 numeros, imprima en pantalla cual es el mayor, el menor, cuales son iguales y si los tres son diferentes

#Digitar los numeros

num1 = int(input("Digite el valor 1: "))
num2 = int(input("Digite el valor 2: "))
num3 = int(input("Digite el valor 3: "))

#Verificamos si los tres numeros son iguales

if num1 == num2 == num3:
    print("Los tres numeros son iguales: ", num1)
    
else:
    #determinamos el mayor de los tres numeros
    mayor = max(num1, num2, num3)
    #determinamos el menor de los tres numeros
    menor = min(num1, num2, num3)

    #imprimimos
    print("el numero mayor es: ", mayor)
    print("el numero menor es: ", menor)

    #verificamos si algunos son iguales
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Algunos numeros son iguales.")
    else:
        print("Los tres numeros son diferentes")