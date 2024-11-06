#sacar el promedio de las dos calificaciones mas altas de entre tres a,b,c
#calcular la nota final

a= float(input("Digite la nota 1: "))
b= float(input("Digite la nota 2: "))
c= float(input("Digite la nota 3: "))

#sacar el promedio de las dos notas mas altas

if a>b and a>c:
    if b > c:
        prom_notas = (a + b)/2
        print("Su nota final es: ", prom_notas)
elif b>a and b>c:
    if a > c:
        prom_notas1 = (b + a)/2
        print("Su nota final es: ", prom_notas1)
else:
    if a > b:
        prom_notas2 = (c + a)/2
        print("Su nota final es: ", prom_notas2)
    else:
        prom_notas3 = (c + b)/2
        print("Su nota final es: ", prom_notas3)