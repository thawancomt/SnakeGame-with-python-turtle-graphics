import turtle
import random
import time


class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.length = 1 # Initial lenght
        self.snake_body : list[turtle.Turtle] = [self]
        self.point = 0

        self.set_snake_details()

    def set_snake_details(self):  #draw the new head
        self.penup()
        self.shape('square')
        self.color('orange')
        self.showturtle()


    
        
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('white')
        
        self.score = 0
        self.high_score = self.get_high_score()
        
        self.write_score()
    
    def write_score(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def update_score(self):
        self.clear()
        self.check_score_greater_than_high_score()
        self.write_score()

    def increase_score(self):
        self.score += 1
        
    def check_score_greater_than_high_score(self):
        if self.score > self.high_score:
            self.color('red')
            return True
            
    def save_high_score(self):
        if self.check_score_greater_than_high_score():
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
    
    def get_high_score(self):
        try:
            with open('high_score.txt', mode='r') as file:
                self.high_score = int(file.read())
                
        except FileNotFoundError:
            return 0
        return self.high_score






class Game_Engine():
    def __init__(self, DEBUG = False):
        
        self.DEBUG = DEBUG
        
        # Game Scren
        self.screen = turtle.Screen()
        self.screen.title('Snake Game')
        self.screen.tracer(0)
        
        self.screen.bgcolor('blue')
        self.screen.screensize(700, 700)
        self.screen.setup(width=700, height=700)
        
        # Properties to help with game logic
        self.game_screensize_to_set_limit = (-300, 300)
        
        # add apple shape
        self.screen.register_shape('apple_.gif')
        
        # Create Snake
        self.snake = Snake()
        self.create_snake_body()
        
        
        # Food
        
        self.food = Food()
        self.food.shape('apple_.gif')
        self.food.shapesize(stretch_wid=2, stretch_len=2)
        self.food.showturtle()

        # Resize the GIF image
        self.player_point = 0
        
        # Score
        self.score = Score()
        
        
        # Initialize the controls
        self.game_controls()
        
        self.is_game_on = True
        
        
        # Draw the border
        self.draw_border()
        
        self.run()
    
        
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
        
    def create_snake_body(self):
        self.body_positions = [[-20, 0], [-40, 0]]
        
        if self.DEBUG:
            print(f'{len(self.body_positions)} segments added to the snake body at {self.body_positions}')
        
        for position in self.body_positions:
            new_segment = Snake()
            new_segment.goto(position)
            self.snake.snake_body.append(new_segment)
            
    def draw_border(self):
        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.color('white')
        self.border.penup()
        self.border.goto(290, 290)
        self.border.pendown()
        self.border.pensize(5)
        for i in range(4):
            self.border.right(90)
            self.border.forward(600)
            
    def increase_player_point(self):
        self.score.increase_score()
        self.score.update_score()
            
    def increase_snake_lenght(self):
        new_segment = Snake()
        new_segment.goto(self.snake.snake_body[-1].position())
        self.snake.snake_body.append(new_segment)
        
        if self.DEBUG:
            print(f'Snake lenght: {len(self.snake.snake_body)}')
        
            
    def positionate_food(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.food.goto(new_x, new_y)
        
        if self.DEBUG:
            print(f'Food position: {self.food.position()}')

            
    def game_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.go_snake_up, 'Up')
        self.screen.onkeypress(self.go_snake_down, 'Down')
        self.screen.onkeypress(self.go_snake_right, 'Right')
        self.screen.onkeypress(self.go_snake_left, 'Left')
        
    def set_game_over(self):
        self.is_game_on = False
        
        self.screen.bgcolor('black')
        self.screen.title('Game Over')
        
        self.score.save_high_score()
        
        
    def check_collision_with_food(self):
        if self.snake.distance(self.food) < 15:
            self.increase_player_point()
            self.positionate_food()     
            self.increase_snake_lenght()
            
    def check_collision_with_border(self):
        if self.snake.xcor() > 300  - 20 or self.snake.xcor() < -300 + 20 :
            self.set_game_over()
        elif self.snake.ycor() > 300  - 20 or self.snake.ycor() < -300 + 20 :
            self.set_game_over()
            
    def check_colision_with_tail(self):
        for segmente in self.snake.snake_body[1:]:
            if self.snake.distance(segmente) < 15:
                if self.DEBUG:
                    print(f'index',self.snake.snake_body.index(self.snake))
                    print(f'index',self.snake.snake_body.index(segmente))
                    print(f'distance: {self.snake.distance(segmente)}')
                    print(segmente.position(), self.snake.position())
                self.set_game_over()
                
    def check_all_colisions(self) -> None:
        self.check_colision_with_tail()
        self.check_collision_with_border()
        self.check_collision_with_food()
                
    def move_snake(self):
        for segmente in range(len(self.snake.snake_body) -1 , 0, -1):
            new_x = self.snake.snake_body[segmente - 1].xcor()
            new_y = self.snake.snake_body[segmente - 1].ycor()
            self.snake.snake_body[segmente].goto(new_x, new_y)
            
        self.snake.forward(20)
        self.check_all_colisions()
                
                
    def __repr__(self) -> str:
        return f'Game Engine'
    
    def __enter__(self):
        return self.screen.screensize()

    def __exit__(self, exc_type, exc_value, traceback):
        self.screen.bye()
        
    def run(self):
        while self.is_game_on:
            self.screen.update()
            self.move_snake()
            time.sleep(0.1)
        self.screen.exitonclick()





a = Game_Engine(DEBUG=True)