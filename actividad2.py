from turtle import *
from random import randrange, choice
from freegames import square, vector

#definir colores
colors = ['pink', 'purple', 'green', 'blue', 'yellow']

# Elegir colores aleatorios para la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # verificar si la serpiente está en los límites 
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # si la serpiente come la comida, generar nueva posición de comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # la comida se mueve
    move_food()
    
    # limpiar la pantalla 
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def move_food():
    #función que mueve la comida
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    step = choice(directions)
    new_position = food + step

    # Verificar que la nueva posición esté dentro de los límites
    if inside(new_position):
        food.move(step)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()