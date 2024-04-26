import turtle
import random


class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.length = 1 # Initial lenght
        self.snake_body : list[turtle.Turtle] = [self]
        self.point = 0

        self.create_snake_head()

    def move_snake(self):
        for index in range(len(self.snake_body), 1):
            new_x, new_y = self.snake_body[index - 1].position()
            self.snake_body[index].goto(new_x, new_y)

        self.forward(10)
    def up(self):
        if self.heading() != 90:
            self.setheading(90)      #up

    def down(self):
        if self.heading() != 270:
            self.setheading(270)      #down

    def right(self):
        if self.heading() != 0:
            self.setheading(0)   #right

    def left(self):
        if self.heading() != 180:
            self.setheading(180)     #left

    def create_snake_head(self):  #draw the new head, erase the previous tail
        self.penup()
        self.color('orange')
        self.shape('square')
        self.showturtle()

    def check_eat_condition(self, fd):
        if self.distance(fd) < 20:
            return True

    def increase_snake_lenght(self):
        self.length += 1

        t = turtle.Turtle()
        t.penup()
        t.color('orange')
        t.shape('square')
        t.hideturtle()
        self.snake_body.append(t)


    def check_colision_with_tail(self):
        for seg in self.snake_body[1::]:
            if self.distance(seg) < 20:
                return True

    def increasePoint(self):
        self.point += 5




# 'main' starts from here


screen = turtle.Screen()
screen.bgcolor('blue')
screen.setup(550, 650)

border = turtle.Turtle()
border.hideturtle()
border.color('white')
border.speed(0)
border.penup()
border.setposition(250, 250)
border.pensize(5)
border.pendown()
for i in range(4):
    border.right(90)
    border.forward(500)

snake = Snake()


screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')


a = True
while a:
    while True:
        snake.move_snake()
        screen.update()

screen.exitonclick()