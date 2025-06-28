from snake import Snake
from food import Food
from screen import Game_Screen


class Debug():
    """
    A class to help with debugging the Snake game.
    
    This class provides methods for printing debug information to the console.
    """
    def __init__(self, snake, screen, food) -> None:
        """
        Initializes the Debug object.

        Args:
            snake (turtle.Turtle): The snake object.
            screen (turtle._Screen): The game screen.
            food (turtle.Turtle): The food object.
        """
        self.snake : Snake = snake
        self.screen : Game_Screen = screen
        self.food : Food = food

    def snake_pos(self):
        """Returns the snake's position and heading."""
        return f'Snake pos {self.snake.position()} at heading {self.snake.heading()}'
    
    def snake_body(self):
        """Returns the length of the snake's body."""
        return f'Snake body has length {len(self.snake.snake_body)}'

    def food_pos(self):
        """Returns the food's position."""
        return f'Food pos {self.food.position()}'

    def food_distance(self):
        """Returns the distance between the snake and the food."""
        return f'Food distance {self.snake.distance(self.food)}'