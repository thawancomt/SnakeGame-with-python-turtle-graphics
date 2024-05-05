import turtle

class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body : list[turtle.Turtle] = [self]

        self.set_snake_properties()
    
    def set_snake_properties(self):  #draw the new head
        self.penup()
        self.shape('snake_assets/snake_head_0.gif')
        self.color('green')
        self.showturtle()
    
    def create_snake_body(self):
        self.body_positions = [[-20, 0], [-40, 0]]
        
         
        for position in self.body_positions:
            self.increase_snake_lenght()
            
    def increase_snake_lenght(self):
        new_segment = Snake()
        
        new_segment.shape('circle')
        new_segment.shapesize(0.8, 0.8)
        new_segment.color('white')
        
        x, y = self.snake_body[-1].position()
        new_segment.goto(x, y)
        self.snake_body.append(new_segment)
        
    def __call__(self):
        print('22')