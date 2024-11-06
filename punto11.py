#condicion para aceptar o rechazar una pieza en forma de varilla
#criterios son:
#a. longitud mayor a 7.5 cm y no exceder los 9 cm
#b. diametro no menor a 0.5cm ni mayor de 1.3 cm
#c. masa no exceder los 5.8 cm
#nota / masa = a diametro * longitud/densidad; densidad = 3.5 gr/cm

#Definimos la densidad
densidad = 3.5

#capturamos los datos de las piezas
longitud = float(input("Ingresa la longitud de la varilla en cm: "))
diametro = float(input("Ingresa el diámetro de la varilla en cm: "))

#Calcular la masa usando la formula dada

masa = (diametro * longitud)/densidad

#verificar cada criterio de aceptacion
if 7.5 < longitud <= 9.0:
    if 0.5 <= diametro <= 1.3:
        if masa <= 5.8:
            print ("La pieza es aceptada")
        else:
            print("La pieza es rechazada: la masa excede el limite permitido")
    else:
        print("La pieza es rechazada: el diametro esta fuera del rango permitido")
else:
    print("La pieza es rechazada: la longitud esta fuera del rango permitido")