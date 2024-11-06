# Capturar tres números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

# Verificar si uno de los números es divisible por otro
if a != 0 and (b % a == 0 or c % a == 0):
    print(f"{a} es divisor de {b}" if b % a == 0 else f"{a} es divisor de {c}")
elif b != 0 and (a % b == 0 or c % b == 0):
    print(f"{b} es divisor de {a}" if a % b == 0 else f"{b} es divisor de {c}")
elif c != 0 and (a % c == 0 or b % c == 0):
    print(f"{c} es divisor de {a}" if a % c == 0 else f"{c} es divisor de {b}")
else:
    print("Ninguno de los números es divisor de otro.")
