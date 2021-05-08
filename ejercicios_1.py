from math import *

"""
number1 = int(input('Ingrese el primer número: '))
number2 = int(input('Ingrese el segundo número: '))

def media_aritmetica(n1, n2):
    return (n1 + n2) / 2

def media_geometrica(n1, n2):
    return sqrt(n1 * n2)

 
print("La media aritmética es: ", media_aritmetica(number1, number2))
print("La media geométrica es: ", round(media_geometrica(number1, number2), 3)) 


horas = int(input('Cuantas horas vas a trabajar: '))
pago_x_hora = float(input('El pago que vas a recibir por las horas trabajadas: '))

def sueldo_neto(h, p):
    return (h * p)

print("Tu sueldo neto sin impuesto es: ", sueldo_neto(horas, pago_x_hora))
print("Tu sueldo neto con impuesto es: ", 0.75 * sueldo_neto(horas, pago_x_hora))


print('Hallar el presupuesto asignado a cada área: Ginecología, Pediatría y Traumatología')
presupuesto_total = int(input('Presupuesto total a invertir en el hostpital: '))
ginecologia = presupuesto_total * .45
pediatria = presupuesto_total * .30
traumatologia = presupuesto_total * .25

print('El presupuesto de Ginecología es: ', ginecologia)
print('El presupuesto de Pediatría es: ', pediatria)
print('El presupuesto de Traumatología es: ', traumatologia)


sumDigit, extNum = 0, 0

numEntero = int(input("Ingrese un numero entero: "))

while numEntero != 0:
    extNum = numEntero % 10
    print(numEntero)
    numEntero //= 10
    sumDigit += extNum

print("La suma de los digitos es: {}".format(sumDigit))


num = int(input('Ingrese su número: '))
if num % 2 == 0:
    print(num, 'es par.')
else:
    print(num, 'es impar.')
"""

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
