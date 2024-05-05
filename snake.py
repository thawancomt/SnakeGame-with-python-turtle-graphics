import turtle

class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body : list[turtle.Turtle] = [self]

        self.set_snake_properties()
    
    def set_snake_properties(self):  #draw the new head
        self.penup()
        self.shape('square')
        self.color('orange')
        self.showturtle()
    
    def create_snake_body(self):
        self.body_positions = [[-20, 0], [-40, 0]]
        
         
        for position in self.body_positions:
            new_segment = Snake()
            new_segment.goto(position)
            self.snake_body.append(new_segment)
            
        
    def __call__(self):
        print('22')