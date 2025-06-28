import turtle

class Game_Controller():
    """
    A class to manage the game controls.
    
    This class is responsible for handling player input and controlling the
    snake's movement.
    """
    def __init__(self, screen, snake, DEBUG = False):
        """
        Initializes the Game_Controller object.

        Args:
            screen (turtle._Screen): The game screen.
            snake (turtle.Turtle): The snake object.
            DEBUG (bool, optional): Whether to run the game in debug mode. 
            Defaults to False.
        """
        self.screen : turtle._Screen = screen
        self.snake : turtle.Turtle = snake
        self.DEBUG = DEBUG
        self.snake_turning = False
        self.game_controls()
        self.keys_pressed = []
        
    
    def game_controls(self):
        """Sets up the game controls."""
        self.screen.listen()
        self.screen.onkeypress(self.go_snake_up, 'Up')
        self.screen.onkeypress(self.go_snake_down, 'Down')
        self.screen.onkeypress(self.go_snake_right, 'Right')
        self.screen.onkeypress(self.go_snake_left, 'Left')

        
    def go_snake_up(self):
        """Moves the snake up."""
        if self.snake.heading() != 270 and len(self.keys_pressed) == 0:
            self.keys_pressed.append('up')
            self.snake.setheading(90)
            self.snake.shape('snake_assets/snake_head_90.gif') # Change the shape to correspond heading

    def go_snake_down(self):
        """Moves the snake down."""
        if self.snake.heading() != 90 and len(self.keys_pressed) == 0:
            self.keys_pressed.append('down')
            self.snake.setheading(270)
            self.snake.shape('snake_assets/snake_head_270.gif')
            

    def go_snake_right(self):
        """Moves the snake right."""
        if self.snake.heading() != 180 and len(self.keys_pressed) == 0:
            self.keys_pressed.append('right')
            self.snake.setheading(0)
            self.snake.shape('snake_assets/snake_head_0.gif')

    def go_snake_left(self):
        """Moves the snake left."""
        
        if self.snake.heading() != 0 and len(self.keys_pressed) == 0:
            self.keys_pressed.append('left')
            self.snake.setheading(180)
            self.snake.shape('snake_assets/snake_head_180.gif')
    