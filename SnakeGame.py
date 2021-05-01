import turtle
import random


class Snake:
    def __init__(self):
        self.length = 1
        self.direction = 1                     #1 means up
        self.snake_list = [ [0,0], [0, -20] ]  #keeping the extra element on purpose...to 'add' it and increase length after eating
        self.last_deleted_position = [0, 0]    #keeping it for eating condition...to add the 'tail' again after erasing to increase length
        self.point = 0

    def updatePositionForMoving(self):
        if self.direction == 1:          #up
            self.snake_list.insert(0, [self.snake_list[0][0], self.snake_list[0][1] + 20])
        elif self.direction == 2:        #right
            self.snake_list.insert(0, [self.snake_list[0][0] + 20, self.snake_list[0][1]])
        elif self.direction == 3:       #down
            self.snake_list.insert(0, [self.snake_list[0][0], self.snake_list[0][1] - 20])
        elif self.direction == 4:       #left
            self.snake_list.insert(0, [self.snake_list[0][0] - 20, self.snake_list[0][1]])

        self.last_deleted_position = self.snake_list.pop()      #

    def up(self):
        if self.direction != 3:
            self.direction = 1      #up

    def down(self):
        if self.direction != 1:
            self.direction = 3      #down

    def right(self):
        if self.direction != 4:
            self.direction = 2      #right

    def left(self):
        if self.direction != 2:
            self.direction = 4      #left

    def showTheSnake(self):  #draw the new head, erase the previous tail

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('orange')
        t.shape('square')
        t.speed(0)
        t.setposition(self.snake_list[0][0], self.snake_list[0][1])
        t.showturtle()

        x = self.snake_list[self.length-1][0]
        y = self.snake_list[self.length-1][1]
        e = turtle.Turtle()
        e.hideturtle()
        e.penup()
        e.speed(0)
        e.setposition(x, y)
        e.color('blue', 'blue')     #actualy erasing by making a turtle with the color of the background color of screen
        e.shape('square')
        e.showturtle()



    def checkEatCondition(self, fd):
        if self.snake_list[0][0] == fd.x_cor and self.snake_list[0][1] == fd.y_cor:
            return True

    def increaseLengthAndUpdateList(self):
        self.length = self.length + 1
        self.snake_list.insert(self.length, self.last_deleted_position)

    def checkKillCondition(self):
        if(self.snake_list[0][0] >= 250 or self.snake_list[0][0] <= -250 or
                self.snake_list[0][1] >= 250 or self.snake_list[0][1] <= -250):
            return True

        to_find = self.snake_list[0]
        l = self.length-1
        for i in range(1, l):
            if self.snake_list[i] == to_find:
                return True

        return False

    def increasePoint(self):
        self.point = self.point + 5


class Food:
    def __init__(self):
        self.x_cor = random.randrange(-240, 241, 20)
        self.y_cor = random.randrange(-240, 241, 20)

    def showFood(self):
        self.f = turtle.Turtle()
        self.f.hideturtle()
        self.f.penup()
        self.f.color('yellow')
        self.f.speed(0)
        self.f.setposition(self.x_cor, self.y_cor)
        self.f.shape('circle')
        self.f.showturtle()

    def erasePreviousFood(self):
        self.f.clear()





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

point_pen = turtle.Turtle()
point_pen.penup()
point_pen.speed(0)
point_pen.color('orange')
point_pen.hideturtle()
point_pen.setposition(0, 275)
point_pen.write("Point: 0", align='center', font=('arial', 20, 'normal') )

snake = Snake()
food = Food()
food.showFood()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')

while True:
    while True:
        snake.updatePositionForMoving()
        snake.showTheSnake()
        if snake.checkKillCondition() == True:
            break
        if snake.checkEatCondition(food) == True:
            food.erasePreviousFood()
            snake.increaseLengthAndUpdateList()
            snake.increasePoint()
            point_pen.clear()
            point_pen.write("Point: {}" .format(snake.point), align='center', font=('arial', 20, 'normal') )
            food = Food()
            food.showFood()


    pen_dead = turtle.Turtle()
    pen_dead.penup()
    pen_dead.color('red')
    pen_dead.speed(0)
    pen_dead.hideturtle()
    pen_dead.write("DEAD!", align = 'center', font = ('arial', 30, 'normal'))
    break

screen.exitonclick()
