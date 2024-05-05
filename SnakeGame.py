import random
import time
from snake import Snake
from food import Food
from score import Score
from screen import Game_Screen
from game_controls import Game_Controller
from debug import Debug


class Game_Engine():
    def __init__(self, DEBUG = False):
        
        self.DEBUG = DEBUG
        self.difficulty = 0.1
        
        # Game Screen
        self.screen = Game_Screen().screen
        
             
        # Create Snake
        self.snake = Snake()
        self.snake.create_snake_body()
        
        # Food
        self.food = Food()
        self.positionate_food()
        
        # Score
        
        
        # Score
        self.score = Score()
        
        self.is_game_on = True
        
        self.game_controls = Game_Controller(self.screen, self.snake)
        
        self.run_game()
            
            
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
                    pass
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
        
    def run_game(self):
        while self.is_game_on:
            print(Debug(self.snake, self.screen, self.food).snake_pos())
            self.move_snake()
            self.screen.update()
            time.sleep(0.1)
        
        self.screen.mainloop()





a = Game_Engine()