#Desarrollar un algoritmo que lea un numero si es negativo lo imprima junto con su positivo

numero = float(input("Digite su numero: "))

#verificamos si el numero es negativo

if numero < 0:
    #imprimimos el numero negativo
    print("Su numero es negativo ya que su valor es: ", numero)
    #imprimimos el valor positivo del numero
    print("Su numero en valor positivo es: ", -numero)

