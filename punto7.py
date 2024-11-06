#leer un registro con nombre, edad, sexo, el estado civil de cualquier persona e imprimir el nombre de la persona, si corresponde a un hombre
# casado mayor de 40 años o una mujer soltera menor a 50 años

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
sexo = input("Ingresa el sexo (M para masculino, F para femenino): ").upper()
estado_civil =input("Ingresa el estado civil (casado/soltero): ").lower()

#verificar si cumple con alguna de las dos condiciones

if (sexo == "M" and estado_civil == "casado" and edad > 40):
    print("Nombre: ", nombre)
elif (sexo == "F" and estado_civil == "soltero" and edad < 50):
    print("Nombre: ", nombre)
else:
    print("La persona no cumple con los criterios especificados")