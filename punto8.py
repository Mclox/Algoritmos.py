#imprimir el numero medio de entre 3 numeros unicos

num1 = float(input("Digite el primer valor: "))
num2 = float(input("Digite el segundo valor: "))
num3 = float(input("Digite el tercer valor: "))

#identificar cual es el numero medio
if (num1>num2 and num1< num3) or (num1<num2 and num1>num3):
    print("El numero medio es: ", num1)
elif (num2>num1 and num2< num3) or (num2<num1 and num2>num3):
    print("El numero medio es: ", num2)
else:
    print("El numero medio es: ", num3)