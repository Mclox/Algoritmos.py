import math
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

d = (b*b) - (4*a*c)

if d < 0:
    print("La ecuacion no tiene solcuion real")
else:
    x1 = (-b + math.sqrt(d) / (2*a))
    x2 = (-b - math.sqrt(d) / (2*a))
    print("Las soluciones reales de la ecuacion son: x1 =", x1, "y x2 =", x2)