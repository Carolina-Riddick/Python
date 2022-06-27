'''
Ejercicio 1:

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Digite numero 2:"))
num3 = int(input("digite numero 3:"))

print(f"{num1}*3*({num2}*2-2*{num1}*{num3})/2*{num2}")
resultado = (num1 ** 3 * (num2*2 - 2*num1*num3)) / (2*num2)
print(f"El resultado es : {resultado}")

a = float(input("Ingrese un numero"))
b = float(input("Ingrese un numero"))
c = float(input("Ingrese un numero"))
resultado = (a ** 3 * (b**2 - 2 * a*c)) / (2*b)
print(f"El resultado es : {resultado}")

          Sintais simplificada con el operador Ternario. Se recomienda si el codigo es MUY PEQUEÑO
NO SE USA EL ELIF
condicion = False
print("condicion verdadera") if condicion else print ("condicion falsa")
'''
import math

# Ejercicio 2: Determinar la solución lógica de la siguiente operación.
# ((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

a = "(3 + 5 x 8 ) < 3"
b = "((-6)/3 x 4 ) + 2 < 2))"
c = "(a > b)"

print(input("ingrese a b o c: "))
print(input("Ingrese a b o c: "))

if a and b or c:
    print("El resultado es verdadero")
else:
    print("el resultado es Falso")
print("")

'''Ejercicio 3:
Intercambiar el valor de dos variables.
Por ejemplo:
a = 10        a = 5
b = 5         b = 10
'''

a = 10
b = 5
aux = int
print(f"Los valores son a:{a} y b: {b} ")

aux = a
a = b
b = aux
print(f'''Los nuevos valores son: 
    a:{a}
    b:{b}
                               ''')
'''
#Ejercicio 4: Área y longitud de un circulo. Hacer un programa para ingresar el radio de un circulo y se reporte su
área y la longitud de la circunferencia.

Área = Pi * r2
Longitud = 2 * Pi * r
En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi. Se escribe:   import math
'''
radio = float(input("Ingrese el radio de un circulo: "))
area = (math.pi * (radio ** 2))
longitud= 2 * math.pi * radio

print(f''' 1. El area del circulo es de: {area},
 2. La longitud del circulo es de: {longitud}
                ''')