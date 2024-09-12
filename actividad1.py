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
    turtle.circle(radius)
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

# Actividad 2. Juego de la Víbora



# Actividad 3. Juego del Packman



# Actividad 4. Juego del Tiro Parabólico



# Actividad 5. Juego de Memoria
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()


"""
    Referencias de código implementados:
    1.-https://grantjenks.com/docs/freegames/paint.html
    2.-http://www.grantjenks.com/docs/freegames/snake.html
    3.-http://www.grantjenks.com/docs/freegames/pacman.html
    4.-http://www.grantjenks.com/docs/freegames/cannon.html
    5.-https://grantjenks.com/docs/freegames/memory.html
""" 