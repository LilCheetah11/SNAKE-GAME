from turtle import Turtle,Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    #collision with food

    if snake.segments[0].distance(food)<20:
        
        food.refresh()
        snake.extend_snake()
        scoreboard.clear()
        scoreboard.increase_score()
    
    #collision with wall

    if snake.segments[0].xcor() >290 or snake.segments[0].xcor() <-290 or snake.segments[0].ycor() >290 or snake.segments[0].ycor() <-290:
        scoreboard.clear()
        scoreboard.reset()
        snake.reset()

    #Detect collision with snake's tail
    for segment in snake.segments[1:]:    
        if snake.segments[0].distance(segment) < 10:
            scoreboard.clear()
            scoreboard.reset()
            
            snake.reset()







screen.exitonclick()




