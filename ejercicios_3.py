# Descomentar cada fragmento del código uno por uno para no tener errores.


# 1.- Escribir un algoritmo que permita determinar si un número es múltiplo de otros dos números a la vez.


""" print('\n       MULTIPLOS DE UN NÚMERO\n')
number = int(input('Escriba el número que desee: '))
m1 = number * 2
m2 = number * 3
print('\n', number, ' es múltiplo de: ', m1, ' y ', m2)  """






# 2.- Escribir un programa que dados 3 números determine cuál es el mayor.

""" 
print('\n       EL NÚMERO MAYOR\n')
n1 = int(input('Primer número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Tercer número: '))

if n1 > n2 and n2 > n3:
    print('\nEl número mayor es: ', n1)
elif n2 > n1 and n1 > n3:
    print('\nEl número mayor es: ', n2)
else:
    print('\nEl número mayor es: ', n3) 



    
 """

# 3.- En un plan de telefonía cada minuto de llamada cuesta S/. 0.40 si esta se realiza en el día y S/. 0.30 si esta se
# realiza de noche. Este plan viene con 20 minutos libres sólo para llamadas de día, no hay minutos libres para
# llamadas de noche. Elabore un programa que permita determinar el costo de un cliente dado el total de minutos
# llamados de día y el total de minutos llamados de noche (ambos datos pedidos al usuario). 

""" print('\n       GASTO DE LAS LLAMADAS\n')
dia = int(input('¿Cúantos minutos piensa llamar en durante el día? '))
noche = int(input('¿Cúantos minutos piensa llamar en durante la noche? '))

gratis_dia = 20

gasto_dia = 0
gasto_noche = noche * .3

if dia > gratis_dia:
    gasto_dia += (dia - gratis_dia) * .4

gasto_total = gasto_dia + gasto_noche
print('En el día va a gastar: ', round(gasto_dia, 2))
print('En la noche va a gastar: ', round(gasto_noche, 2))
print('Por lo tanto, al final del día va a pagar: ', round(gasto_total, 2)) """





# 4.- Escriba una función que dada una posición x,y y un tamaño de lado dibuje en la pantalla la figura mostrada:


from turtle import *

print('\n       DIBUJANDO UN CUADRADO INCRUSTADO EN OTRO\n')
x = int(input('Escriba la posición x del dibujo: '))
y = int(input('Escriba la posición y del dibujo: '))
l = int(input('Escriba la logitud del lado del cuadrado: '))


# Dibujando el cuadrado exterior

penup()
goto(x, y)
pendown()

forward(l)
right(90)
forward(l)
right(90)
forward(l)
right(90)
forward(l)
right(90)

# Dibujando el cuadrado interior
penup()
goto(x+20, y-20)
pendown()

forward(l-40)
right(90)
forward(l-40)
right(90)
forward(l-40)
right(90)
forward(l-40)
right(90)

input('Press Enter para salir...')