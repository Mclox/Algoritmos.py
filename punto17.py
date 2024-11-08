# Leer tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Verificar divisibilidad entre los números
if num1 % num2 == 0:
    print(f"{num1} es divisible por {num2}")
elif num1 % num3 == 0:
    print(f"{num1} es divisible por {num3}")
elif num2 % num1 == 0:
    print(f"{num2} es divisible por {num1}")
elif num2 % num3 == 0:
    print(f"{num2} es divisible por {num3}")
elif num3 % num1 == 0:
    print(f"{num3} es divisible por {num1}")
elif num3 % num2 == 0:
    print(f"{num3} es divisible por {num2}")
else:
    print("Ninguno de los números es divisible por otro.")

