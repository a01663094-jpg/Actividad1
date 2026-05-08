"""Paint modificado.

Cambios realizados:
1. Se agregaron más colores.
2. Se completó la función circle.
3. Se completó la función rectangle.
4. Se completó la función triangle.
5. Se agregó cambio de grosor con teclas.
"""

from turtle import *
from freegames import vector


def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_draw(start, end):
    up()
    goto(start.x, start.y)
    down()

    radius = abs(end.x - start.x)

    begin_fill()
    circle(radius)
    end_fill()


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width_rect = end.x - start.x
    height_rect = end.y - start.y

    for count in range(2):
        forward(width_rect)
        left(90)
        forward(height_rect)
        left(90)

    end_fill()


def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(end.x, start.y)
    goto((start.x + end.x) / 2, end.y)
    goto(start.x, start.y)

    end_fill()


def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    state[key] = value


def change_width(amount):
    new_width = state['width'] + amount

    if new_width < 1:
        new_width = 1

    state['width'] = new_width
    width(new_width)

    print("Grosor actual:", new_width)


state = {
    'start': None,
    'shape': line,
    'width': 5,
}

setup(420, 420, 370, 0)
hideturtle()
listen()

width(state['width'])

onscreenclick(tap)

# Figuras
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_draw), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't'

# Colores
onkey(lambda: color('black'), 'k')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'e')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('yellow'), 'y')
onkey(lambda: color('purple'), 'p')
onkey(lambda: color('orange'), 'o')
onkey(lambda: color('pink'), 'i')
onkey(lambda: color('brown'), 'n')

# Grosor onkey(lambda: change_width(1), 'Up')
onkey(lambda: change_width(-1), 'Down')

done()
