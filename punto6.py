#Capturar el valor ingresado por el usuario

entrada = str(input("Ingresa un valor: "))

#Convertir de grados celsius a kelvin
numero_entero = int(entrada)
kelvin = numero_entero + 273.15
print("el valor en grados Kelvin es: ", kelvin)

numero_float = float(kelvin)

#condiciones
if numero_float > 10.5:
    print("su valor en grados kelvin es mayor a 10.5")
elif numero_float <= 10.5:
    print("El numero flotante es menor o igual a 10.5")
#si no es entero ni flotante asumir que es un caracter
else:
    #pedir el nombre al usuario
    nombre = input("Parece que ingresaste un caracter. Ingresa tu nombre: ")
    print("El nombre ingresado es: ", nombre)