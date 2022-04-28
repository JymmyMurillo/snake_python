from turtle import Screen

from sqlalchemy import false
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# Crear el escenario
screen = Screen()  # Instanciar objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate Snake")

screen.tracer(0)  # Quitamos animacion de movimiento

#crear - instanciar objeto serpiente
snake = Snake()

#crear - instanciar objeto comida
food = Food()

#crear - instanciar objeto tablero de puntos
scoreboard = Scoreboard()

#Movimientos serpiente
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    
    #Detectar colision con comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increased_score()
        snake.extend()

    #Derectar las paredes
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
        
    #Detectar colision de la cola
    for segment in snake.segments[1:]:
        #if segment == snake.head:
        #    pass
        #elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
