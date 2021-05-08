from turtle import *
import random
import os

def clear_console():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def selection(s):
    if s == 1:
        print('\n       DIBUJO DE FIGURAS \n')
        print('Figuras disponibles para dibujar.')
        print('     [1] Cuadrado')
        print('     [2] Círculo')
        print('     [3] Cubo')
        print('     [4] Cuadrado con color')
        print('     [0] Salir \n')
        return int(input('Elija la figura que desee dibujar: '))
    elif s == 2:
        print('\n       ADIVINA LA PALABRA \n')
        print('Dificultades del juego disponibles.')
        print('     [1] Fácil')
        print('     [2] Intermedio')
        print('     [3] Difícil')
        print('     [0] Salir \n')
        return int(input('Elija la dificultad del juego: '))
    elif s == 3:
        print('\n       CALCULAR SUELDO \n')
        print('Horario en la que trabaja.')
        print('     [1] Diurno')
        print('     [2] Nocturno')
        print('     [0] Salir \n')
        data = []
        data.append(int(input('Elija su horario: ')))
        data.append(int(input('Cantidad de horas a trabajar: ')))
        return data
    elif s == 4:
        print('\n       CALCULAR DESCUENTO \n')
        print('¿En qué año se encuentra?.')
        print('     [1] Primer año')
        print('     [2] Segundo año')
        print('     [3] Tercero año')
        print('     [4] Cuarto año')
        print('     [5] Quinto año')
        print('     [0] Salir \n')
        data = []
        data.append(int(input('Elija el año en que pertenece: ')))
        data.append(float(input('¿Cuánto fue su último puntaje semestral?: ')))
        data.append(float(input('Pensión a pagar: ')))
        return data
    elif s == 5:
        print('\n       ¿QUÉ TRIÁNGULO ES? \n')
        print('Triangulos que el programa conoce.')
        print('     [1] Equilátero')
        print('     [2] Isóceles')
        print('     [3] Escaleno')
        print('     [0] Salir \n')
        data = []
        data.append(float(input('¿Cuánto mide su primer lado?: ')))
        data.append(float(input('¿Cuánto mide su segundo lado?: ')))
        data.append(float(input('¿Cuánto mide su tercer lado?: ')))
        return data
    elif s == 6:
        print('\n       CALENDARIO \n')
        print('¿Qué día es hoy?')
        print('     [1] Lunes')
        print('     [2] Martes')
        print('     [3] Miércoles')
        print('     [4] Jueves')
        print('     [5] Viernes')
        print('     [6] Sabado')
        print('     [7] Domingo')
        print('     [0] Salir \n')
        data = [['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']]
        data.append(int(input('Coloque el día en la que se encuentra hoy: ')))
        data.append(int(input('¿Cuántos días quieres avanzar en el futuro?: ')))
        return data

def reglas():
    clear_console()
    print('\n           ADIVINA LA PALABRA\n')
    print('REGLAS:')
    print('- No olvidar las tildes si la palabra la tiene.')
    print('- Solo tienes 2 pistas, a la tercera se revelará la palabra y perderás.')
    print('- Para la pista envía "1" y se revelará una letra.')
    print('- Para más dificultad cambia las palabras de "i", "m" o "e".')
    print('- Diviértete.\n\n')

def tip(w, s):
    i = random.randint(1, int(len(w)))
    print(i)
    return i  

def quit_app(g):
    if g == 0:
        clear_console()
        exit()
    clear_console()
    print('\n       FIN DEL PROGRAMA \n')
    print('¿Qué desea hacer ahora?')
    print('     [1] Volver a jugar')
    print('     [2] Regresar al menú de los juegos')
    print('     [0] Salir del programa\n')
    select = int(input("\nElija su opción: "))
    if select == 1:
        clear_console()
        if g == 1:
            clear()
            draw()
        elif g == 2:
            guess()
        elif g == 3:
            calculate()
        elif g == 4:
            discount()
        elif g == 5:
            triangle()
        elif g == 6:
            calendar()
        
    elif select == 2:
        if g == 1:
            bye()
            clear_console()
            start_game()
        else:
            clear_console()
            start_game()
    elif select == 0:
        clear_console()
        exit()

def draw_square(l):
    for i in range(4):
        forward(l)
        right(90)

def draw_square_color(l):
    for i in range(4):
        print(i)
        if i >= 1 and i <= 2:
            pencolor('red')
            forward(l)
            right(90)
        else:
            pencolor('green')
            forward(l)
            right(90)

def draw_cube(l, x, y):
    draw_cuadrado(l)
    goto(l//2 + (x), l//2 + (y))
    draw_cuadrado(l)
    goto(l//2 + (x) + l, l//2 + (y))
    goto(l+x,y)
    goto(l+x, -(l-y))
    goto(l//2 + (x) + l,l//2 + (y) - l)
    goto(l//2 + (x),l//2 + (y) - l)
    goto(x, y - l)

def draw_circle(r):
    circle(r)

def draw():
    figura = selection(1)
    if figura > 4 or figura == 0:
        quit_app(0)

    x = int(input('\nEscriba la posición x del dibujo: '))
    y = int(input('Escriba la posición y del dibujo: '))

    penup()
    goto(x, y)
    pendown()

    if figura == 1:
        l = int(input('Escriba la longitud del lado del cuadrado: '))
        draw_square(l)
        quit_app(1)
    elif figura == 2:
        r = int(input('Escriba el radio del círculo: '))
        draw_circle(r)
        quit_app(1)
    elif figura == 3:
        l = int(input('Escriba la longitud del lado del cubo: '))
        draw_cube(l, x, y)
        quit_app(1)
    elif figura == 4:
        l = int(input('Escriba la longitud del lado del cuadrado: '))
        draw_square_color(l)
        quit_app(1)

def select_word_random(w):
    datos = ['dato1', 'dato2', 'dato3']
    word = random.choice(datos)
    return w[word]

def word_select(d):
    lista = {
        'i': {
            'dato1': {
                'word': 'ESTUPEFACTO',
                'tips': [
                    '\n"Antes había proferido algún grito, pero ahora no podía hablar: estaba ________"\n',
                    '\nSinónimo: "Atónito"\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato2': {
                'word': 'ORNITORRINCO',
                'tips': [
                    '\nMamífero que pone huevos.\n',
                    '\n¿Es un castor o un pato?\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato3': { 
                'word': 'ELECTROCARDIOGRAMA',
                'tips': [
                    '\nRegistra las señales eléctricas del corazón.\n',
                    '\nEs una prueba común e indolora que se utiliza para detectar rápidamente los problemas cardíacos y controlar la salud del corazón.\n',
                    '\nYou lose :(\n'
                ]
            },
        },
        'm': {
            'dato1': {
                'word': 'UNIVERSIDAD',
                'tips': [
                    '\nInstitución educativa superior.\n',
                    '\nDespués de la secundario se debería de ir a la __________\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato2': {
                'word': 'INFORMÁTICA',
                'tips': [
                    '\n"Este es un programa ________"\n',
                    '\nRelacionado con la información\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato3': { 
                'word': 'CACHIMBO',
                'tips': [
                    '\n"Corten el cabello al _________"\n',
                    '\nNuevo ingresante de la universidad se le llama:\n',
                    '\nYou lose :(\n'
                ]
            },
        },
        'e': {
            'dato1': {
                'word': 'COMPAÑERO',
                'tips': [
                    '\nSinónimo: Aliado, amigo.\n',
                    '\n"Mi perro es mi fiel _______"\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato2': {
                'word': 'COMPUTADORA',
                'tips': [
                    '\nMáquina capáz de ejecutar programas como este.\n',
                    '\nSi no pudiste mejor cambiate de carrera xD\n',
                    '\nYou lose :(\n'
                ]
            },
            'dato3': { 
                'word': 'UNSA',
                'tips': [
                    '\nUniversidad de Arequipa\n',
                    '\n¿En serio?, ¿2 pistas?\n',
                    '\nYou lose :(\n'
                ]
            },
        }
    }

    if d == 1:
        return select_word_random(lista['e'])
    elif d == 2:
        return select_word_random(lista['m'])
    elif d == 3:
        return select_word_random(lista['i'])

def guess():
    difficult = selection(2)
    if difficult > 3 or difficult == 0:
        quit_app(0)

    word_full = word_select(difficult)
    word = word_full['word']
    index = random.randint(1, int(len(word)))
    secret_word = ''
    for i, w in enumerate(word):
        if i == index and w not in secret_word:
            secret_word += word[i]
            secret_word += ' '
        secret_word += '_ '

    reglas()
    print(secret_word, '\n')
    for i in range(3):
        result = input('La palabra secreta es: ')
        if result == '1':
            tip = word_full['tips'][i]
            print(tip)
            if tip == '\nYou lose :(\n':
                input('Press Enter para continuar...')
                quit_app(2)
        elif result.upper() == word:
            clear_console()
            print('You win :)')
            input('\nPress Enter para continuar...')
            quit_app(2)
            break
        else:
            print('\nPerdiste una pista por no cumplir. :P\n')
                
def calculate():
    data = selection(3)
    horario, horas = data[0], data[1]
    if horario > 2 or horario == 0:
        quit_app(0)
    sueldo = 0
    if horario == 1:
        sueldo += 1250
        sueldo += horas * 15
    elif horario == 2:
        sueldo += 1700
        sueldo += horas * 25

    print('\nSu sueldo será de', sueldo, 'soles.\n')
    input('Press Enter para continuar...')
    quit_app(3)

def discount():
    data = selection(4)
    anyo, promedio, pension = data[0], data[1], data[2]
    if anyo > 5 or anyo == 0:
        quit_app(0)
    if anyo < 3 and promedio > 16.00:
        clear_console()
        print('\nRecibirá un descuento del 10%, ¡Felicidades!')
        print('Ahora tendrá que pagar el monto de total de:', pension * .9)
        input('Press Enter para continuar...')
        quit_app(4)
    elif anyo >= 3 and promedio > 13.50:
        clear_console()
        print('\nRecibirá un descuento del 20%, ¡Felicidades!')
        print('Ahora tendrá que pagar el monto de total de:', pension * .8)
        input('Press Enter para continuar...')
        quit_app(4)
    else:
        clear_console()
        print('\nLo siento, su promedio no acredita un descuento, ¡Sigue intentando!')
        print('tendrá que pagar el monto de total de:', pension)
        input('Press Enter para continuar...')
        quit_app(4)

def triangle():
    triangle = selection(5)
    l1, l2, l3 = triangle[0], triangle[1], triangle[2]
    if l1 == 0 or l2 == 0 or l3 == 0:
        quit_app(0)

    if l1 == l2 and l2 == l3:
        clear_console()
        print('\nEl triángulo es uno con sus lados iguales, entonces es Equilátero.')
        input('Press Enter para continuar...')
        quit_app(5)
    elif l1 == l2 or l1 == l3 or l2 == l3:
        clear_console()
        print('\nEl triángulo es uno con dos de sus lados iguales, entonces es Isóceles.')
        input('Press Enter para continuar...')
        quit_app(5)
    else:
        clear_console()
        print('\nEl triángulo es uno que no tiene lados iguales, entonces es Escaleno.')
        input('Press Enter para continuar...')
        quit_app(5)

def calendar():
    data = selection(6)
    days, now, future = data[0], data[1], data[2]
    if now > 7 or days == 0:
        quit_app(0)
    clear_console()
    print('\nHoy es:', days[now - 1])
    print('Y el día que será dentro de', future, 'días es', days[((future % 7) + now) - 1 ])
    input('Press Enter para continuar...')
    quit_app(6)


def start_game():
    clear_console()
    print('\n       EJERCICIOS EN PYTHON \n')
    print(' INDICACIONES')
    print('- Toda selección en el programa se usa números para evitar crear condicionales de más.')
    print('- El programa usa funciones para reutilizar fragmentos de código.')
    print('- Se reunió algunos ejercicios en un solo juego para no tener una lista larga.')
    print('- Y nada, diviértase :) \n')
    print(' JUEGOS')
    print(' [1] Dibujo de figuras. (1, 2, 3, 6 y 10)')
    print(' [2] Juego de adivina la palabra. (4)')
    print(' [3] Calcular el sueldo según su turno y horas extras. (5)')
    print(' [4] Calcular el descuento de un alumno. (7)')
    print(' [5] Saber qué triángulo es. (8)')
    print(' [6] Saber qué día será. (9) \n')
    select_game = int(input('Seleccione el juego a jugar: '))
    clear_console()

    if select_game == 1:
        draw()
    elif select_game == 2:
        guess()
    elif select_game == 3:
        calculate()
    elif select_game == 4:
        discount()
    elif select_game == 5:
        triangle()
    elif select_game == 6:
        calendar()

start_game()

