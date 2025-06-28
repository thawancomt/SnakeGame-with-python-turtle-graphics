import turtle

class Food(turtle.Turtle):
    """
    A class to represent the food in the Snake game.
    
    This class inherits from the turtle.Turtle class and is responsible
    for creating and displaying the food on the screen.
    """
    def __init__(self):
        """Initializes the Food object."""
        super().__init__()
        self.penup()
        self.shape('apple.gif')
