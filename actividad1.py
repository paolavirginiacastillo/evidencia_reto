"""
    Materia: Herramientas computacionales: el arte de la programación (Gpo 101)
    Profesor Titular: Edoardo Bucheli
    Equipo No.

    Integrantes:
    - Kenia Esmeralda Ramos Javier - A01799073.
    - Paola Virginia Castillo Moccia - A01784854

""" 

from turtle import *
from freegames import vector

# Acitividad 1. Juego Pintando
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y) #vector inicial
    down()
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5 #radio = distancia puntos de inicio y final
    begin_fill()
    circle(radius)
    end_fill() #final

def rectangle(start, end):
    "Draw rectangle from start to end."
    #ancho y alto = diferencia en coordenadas x y y
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for _ in range(2):
        forward(abs(width))  # valor absoluto para asegurar que el ancho sea positivo
        left(90)
        forward(abs(height)) # valor absoluto para asegurar que la altura sea positiva
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # longitud del lado del triángulo
    side_length = abs(end.x - start.x)  # diferencia

    # dibujo de triángulo
    for _ in range(3):
        forward(side_length)
        left(120)  # ángulo triángulo

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'o') #añadir naranja como nuevo color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', triangle), 't')
done()

"""
    Referencias de código implementados:
    1.-https://grantjenks.com/docs/freegames/paint.html
""" 