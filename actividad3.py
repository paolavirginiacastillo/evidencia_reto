from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0) 
pacman = vector(-40, -80)

# Posiciones corregidas de los fantasmas para que aparezcan dentro del laberinto
ghosts = [
    [vector(-100, 160), vector(10, 0)],  # Fantasma 1 en la parte superior izquierda
    [vector(80, 160), vector(0, 10)],   # Fantasma 2 en la parte superior derecha
    [vector(-60, -60), vector(0, -10)],  # Fantasma 3 en la parte inferior izquierda
    [vector(60, 60), vector(-10, 0)],  # Fantasma 4 en la parte inferior derecha
]

# Nuevo diseño del tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    """Dibuja una celda cuadrada usando path en (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    """Devuelve el desplazamiento del punto en tiles, con manejo de límites."""
    x = (floor(point.x, 20) + 200) // 20
    y = (180 - floor(point.y, 20)) // 20
    index = int(x + y * 20)
    
    # Verificamos que el índice esté dentro del rango válido
    if 0 <= index < len(tiles):
        return index
    else:
        return None  # Retorna None si el índice está fuera del rango

def valid(point):
    """Devuelve True si el punto es válido en el tablero."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def move_toward_pacman(ghost, pacman):
    """Mueve los fantasmas hacia Pacman solo por caminos válidos."""
    options = []
    if valid(ghost + vector(5, 0)):  # Derecha
        options.append(vector(5, 0))
    if valid(ghost + vector(-5, 0)):  # Izquierda
        options.append(vector(-5, 0))
    if valid(ghost + vector(0, 5)):  # Arriba
        options.append(vector(0, 5))
    if valid(ghost + vector(0, -5)):  # Abajo
        options.append(vector(0, -5))

    if options:
        # Elegimos la opción que acerca más al fantasma hacia Pacman
        min_distance = float('inf')
        best_option = None

        for option in options:
            new_position = ghost + option
            distance = abs(new_position.x - pacman.x) + abs(new_position.y - pacman.y)
            if distance < min_distance:
                min_distance = distance
                best_option = option

        # Si elige la mejor opción, con probabilidad del 20% cambiará de dirección aleatoriamente para evitar bucles
        if best_option and choice([True, False, False, False, False]):
            return choice(options)
        return best_option
    else:
        # Si no encuentra una dirección hacia Pacman, elige una al azar
        return choice([vector(5, 0), vector(-5, 0), vector(0, 5), vector(0, -5)])

def world():
    """Dibuja el tablero usando path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    """Mueve a Pacman y a los fantasmas."""
    writer.undo()
    writer.write(state['score'])

    clear()

    # Pacman se moverá continuamente si hay un camino válido
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        # Mover fantasmas hacia Pacman solo por caminos válidos
        best_move = move_toward_pacman(point, pacman)
        if valid(point + course):
            point.move(course)
        if best_move:
            course.x = best_move.x
            course.y = best_move.y
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),]

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    """Cambia la dirección de Pacman si es válido."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
