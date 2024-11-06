nota1= float(input("Ingrese la nota 1 (valor de 1.0 a 5.0): "))
nota2= float(input("Ingrese la nota 2 (valor de 1.0 a 5.0): "))
nota3= float(input("Ingrese la nota 3 (valor de 1.0 a 5.0): "))

prom_notas = round((nota1+nota2+nota3)/3, 1)

if 3.5 < prom_notas <= 5.0:
    print("Su nota es: ", prom_notas, "aprobo la materia")
else:
    print("Su nota es: ", prom_notas, "reprobo la materia") 