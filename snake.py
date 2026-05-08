"""Snake modificado.

Cambios realizados:
1. La serpiente empieza quieta hasta presionar una flecha.
2. Se agregó marcador de puntuación.
3. Se agregaron colores personalizados.
4. Se agregó mensaje de Game Over.
5. Se ajustó la velocidad del juego.
"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(0, 0)]
aim = vector(0, 0)
score = 0
game_started = False


def change(x, y):
    """Cambia la dirección de la serpiente e inicia el juego."""
    global game_started
    aim.x = x
    aim.y = y
    game_started = True


def inside(head):
    """Revisa si la serpiente está dentro de la pantalla."""
    return -200 < head.x < 190 and -200 < head.y < 190


def draw_score():
    """Dibuja la puntuación actual."""
    up()
    goto(-190, 170)
    color('black')
    write(f'Score: {score}', font=('Arial', 16, 'normal'))


def move():
    """Mueve la serpiente."""
    global score

    clear()
    draw_score()

    if not game_started:
        up()
        goto(-130, 0)
        color('black')
        write('Press an arrow key to start', font=('Arial', 16, 'normal'))
        square(food.x, food.y, 9, 'red')
        square(snake[0].x, snake[0].y, 9, 'green')
        update()
        ontimer(move, 150)
        return

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        color('red')
        up()
        goto(-80, 0)
        write('GAME OVER', font=('Arial', 24, 'bold'))
        update()
        return

    snake.append(head)

    if head == food:
        score += 1
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    draw_score()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()

    ontimer(move, 150)


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
