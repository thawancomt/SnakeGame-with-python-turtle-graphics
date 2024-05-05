import turtle
class Game_Screen():
    def __init__(self):
        # Game Screen
        self.screen = turtle.Screen()
        self.screen.title('Snake Game')
        self.screen.tracer(0)
        
        self.screen.bgcolor('blue')
        self.screen.screensize(700, 700)
        self.screen.setup(width=700, height=700)
        
        # Properties to help with game logic
        self.game_screensize_to_set_limit = (-300, 300)
        
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
        self.border.goto(290, 290)
        self.border.pendown()
        self.border.pensize(5)
        for i in range(4):
            self.border.right(90)
            self.border.forward(600)