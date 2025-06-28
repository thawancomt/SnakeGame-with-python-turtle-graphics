import turtle
class Game_Screen():
    def __init__(self):
        # Game Screen
        self.screen = turtle.Screen()
        self.screen.title('Snake Game')
        self.screen.tracer(0)
        
        self.screen.bgcolor('blue')
        self.screen.screensize(700, 700)
        self.screen.setup(width=self.screen.screensize()[0], height=self.screen.screensize()[1])

        self.bounding_box_limit = {
            "width" : self.screen.screensize()[0] / 2 - 40,
            "height" : self.screen.screensize()[1] / 2 - 40
        }

        # Properties to help with game logic
        # self.game_screensize_to_set_limit = (-300, 300)
        
        # add apple shape
        self.screen.register_shape('apple.gif')
        
        # add snake shape, each heading has itself gif file
        self.screen.register_shape('snake_assets/snake_head_0.gif')
        self.screen.register_shape('snake_assets/snake_head_90.gif')
        self.screen.register_shape('snake_assets/snake_head_180.gif')
        self.screen.register_shape('snake_assets/snake_head_270.gif')
        

        # Draw the border
        self.draw_border()
        
        
    def draw_border(self):
        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.color('white')
        self.border.penup() 
        self.border.goto(self.bounding_box_limit["width"], self.bounding_box_limit["height"])
        self.border.pendown()
        self.border.pensize(5)

        # Draw the square border
        for i in range(4):
            self.border.right(90)
            self.border.forward(self.bounding_box_limit["width"] * 2)
