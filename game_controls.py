import turtle

class Game_Controller():
    def __init__(self, screen, snake, DEBUG = False):
        self.screen : turtle._Screen = screen
        self.snake : turtle.Turtle = snake
        self.DEBUG = DEBUG
        self.game_controls()
        
    
    def game_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.go_snake_up, 'Up')
        self.screen.onkeypress(self.go_snake_down, 'Down')
        self.screen.onkeypress(self.go_snake_right, 'Right')
        self.screen.onkeypress(self.go_snake_left, 'Left')
    
    def go_snake_up(self):
        if self.DEBUG:
            print('Trying up')
        if self.snake.heading() != 270:
            self.snake.setheading(90)

    def go_snake_down(self):
        if self.DEBUG:
            print('Trying down')
        if self.snake.heading() != 90:
            self.snake.setheading(270)
            

    def go_snake_right(self):
        if self.DEBUG:
            print('Trying right')
        if self.snake.heading() != 180:
            self.snake.setheading(0)

    def go_snake_left(self):
        if self.DEBUG:
            print('Trying left')
        if self.snake.heading() != 0:
            self.snake.setheading(180)
    