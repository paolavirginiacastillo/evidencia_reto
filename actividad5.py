"""
    Materia: Herramientas computacionales: el arte de la programación (Gpo 101)
    Profesor Titular: Edoardo Bucheli
    Equipo No.

    Integrantes:
    - Kenia Esmeralda Ramos Javier - A01799073.
    - Paola Virginia Castillo Moccia - A01784854

    Actividad 5. Juego de Memoria

""" 
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None,'tap_count':0}
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
    state['tap_count'] += 1 #Incrementa el contador.

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    """Verifica que los cuadros(tiles) esten destapados"""
    if all(not hidden for hidden in hide):
        print(f"¡Felicidades! Has ganado en: {state['tap_count']} taps!")
        done()

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
        goto(x + 2, y +2) #Centrar los dígitos
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    """Muestra en la pantalla el contador de taps"""
    up()
    goto(-180,210)
    color('black')
    write(f'Taps: {state["tap_count"]}',font=('Arial',20,'normal'))
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
"""4.- Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?
    Sí, sería más didactico que fueran una especie de imagenes algo llamativos o iconos que ayuden a hacerlo más visual, porque el blanco de las tarjetas y el color de los numeros (en mi opinion fastidia la vista)"""
"""
    Referencias de código implementados:
    5.-https://grantjenks.com/docs/freegames/memory.html
""" 