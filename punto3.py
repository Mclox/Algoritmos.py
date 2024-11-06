#crear un algoritmo que aumente el sueldo del trabajador un 15% si su sueldo es inferior a 300.000$

sueldo_trabajador = float(input("Ingrese su sueldo: "))

#creamos la condicion

if sueldo_trabajador < 300000:
    #calculamos el aumento dwel 15%
    aumento = sueldo_trabajador * 0.15
    #sumamos el aumento al sueldo original
    sueldo_final = sueldo_trabajador + aumento

    #imprimimos el sueldo final

    print("El sueldo del trabajador con aumento es: ", sueldo_final)
    