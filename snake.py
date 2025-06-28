import turtle

class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body : list[turtle.Turtle] = [self]

        self.shape('snake_assets/snake_head_0.gif')

        self.body_dimensions = {
            "width": 1,  # Increased width
            "height": 1  # Increased height
        }

        self.set_snake_properties()

        # Remove turtlesize, use shapesize in set_snake_properties

    
    def set_snake_properties(self):  #draw the new head
        self.penup()
        self.shape('snake_assets/snake_head_0.gif')
        self.color('green')
        self.showturtle()
        self.speed(1)
    
    def create_snake_body(self,):
        # To initial snake body segments
        self.body_positions = [[-20, 0], [-40, 0]]

        for _ in self.body_positions:
            self.increase_snake_lenght()
            
    def increase_snake_lenght(self):
        new_segment = Snake()
        
        new_segment.shape('circle')
        new_segment.shapesize(self.body_dimensions["width"] , self.body_dimensions["height"])
        new_segment.color('white')
        
        x, y = self.snake_body[-1].position()
        new_segment.goto(x, y)
        self.snake_body.append(new_segment)