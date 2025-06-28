import turtle

class Snake(turtle.Turtle):
    """
    A class to represent the snake in the Snake game.
    
    This class inherits from the turtle.Turtle class and is responsible
    for creating and managing the snake's body, as well as its movement
    and appearance.
    """
    def __init__(self):
        """Initializes the Snake object."""
        super().__init__()
        self.snake_body : list[turtle.Turtle] = [self]

        self.shape('snake_assets/snake_head_0.gif')

        self.body_dimensions = {
            "width": 1,  # Increased width
            "height": 1  # Increased height
        }

        self.INITIAL_LENGTH = 3

        self.set_snake_properties()

        self.create_snake_body()

    
    def set_snake_properties(self):
        """Sets the initial properties of the snake's head."""  #draw the new head
        self.penup()
        self.shape('snake_assets/snake_head_0.gif')
        self.color('green')
        self.showturtle()
    
    def create_snake_body(self):
        """Creates the initial body of the snake."""
        # To initial snake body segments
        for _ in range(self.INITIAL_LENGTH):
            self.increase_snake_length()

    def increase_snake_length(self):
        """Increases the length of the snake by one segment."""
        new_segment = turtle.Turtle()
        new_segment.penup()
        
        new_segment.shape('circle')
        new_segment.shapesize(self.body_dimensions["width"], self.body_dimensions["height"])
        new_segment.color('white')
        
        x, y = self.snake_body[-1].position()
        new_segment.goto(x, y)
        self.snake_body.append(new_segment)