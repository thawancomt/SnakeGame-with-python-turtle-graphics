import turtle
from score import Score


class Game_Screen:
    """
    A class to manage the game screen.

    This class is responsible for creating the game screen, setting up its
    properties, and drawing the game border.
    """

    def __init__(self):
        """Initializes the Game_Screen object."""
        # Game Screen
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.screen.screensize(700, 700)
        self.screen.setup(
            width=self.screen.screensize()[0], height=self.screen.screensize()[1]
        )

        self.bounding_box_limit = {
            "width": self.screen.screensize()[0] / 2 - 60,
            "height": self.screen.screensize()[1] / 2 - 60,
        }
        # add apple shape
        self.screen.register_shape("apple.gif")

        # add snake shape, each heading has itself gif file
        self.screen.register_shape("snake_assets/snake_head_0.gif")
        self.screen.register_shape("snake_assets/snake_head_90.gif")
        self.screen.register_shape("snake_assets/snake_head_180.gif")
        self.screen.register_shape("snake_assets/snake_head_270.gif")
        self.screen.register_shape("assets/gameover.gif")

    def show_start_screen(self, callback):
        """
        Sets up the start screen with instructions and high score display.

        Args:
            callback (function): Function to call when the game starts.
        """
        """Sets the initial screen properties for the game."""

        self.screen.tracer(0)

        self.screen.bgcolor("#262626")

        self.screen.title("Snake Game")

        # instructions text are using y 0 to -30
        # high score gonna use y at -50

        def create_title_text():
            title_turtle = turtle.Turtle()
            title_turtle.penup()
            title_turtle.goto(0, 100)
            title_turtle.color("#787878")
            title_turtle.write(
                "SNAKE GAME",
                align="center",
                font=("Press Start 2P", 48, "normal"),
            )
            title_turtle.hideturtle()

        def create_instructions_text():
            start_instructions = turtle.Turtle()
            start_instructions.penup()
            start_instructions.goto(0, 0)
            start_instructions.color("#d3ed2d")
            start_instructions.write(
                "Press Enter to Start or Q to Quit",
                align="center",
                font=("Press Start 2P", 24, "normal"),
            )
            start_instructions.goto(0, -40)
            start_instructions.color("#4f4f4f")
            start_instructions.write(
                "Use Arrow Keys to Control the Snake",
                align="center",
                font=("Press Start 2P", 16, "normal"),
            )
            start_instructions.hideturtle()

        def create_high_score_text():
            high_score_turtle = turtle.Turtle()
            high_score_turtle.penup()
            high_score_turtle.goto(0, -100)
            high_score_turtle.color("white")
            high_score_turtle.write(
                f"High Score: {Score().get_high_score()}",
                align="center",
                font=("Press Start 2P", 16, "normal"),
            )
            high_score_turtle.hideturtle()

        create_title_text()
        create_instructions_text()
        create_high_score_text()

        self.screen.listen()

        self.screen.onkeypress(lambda: callback(), "Return")
        self.screen.onkeypress(lambda: self.screen.bye(), "q")

        self.screen.update()

    def show_game_over_screen(self, score=0, callback=None):
        """ "Sets up the game over screen with final score display."""

        self.screen.clear()
        self.screen.tracer(0)
        self.screen.bgcolor("#1A1A1A")
        self.screen.title("Game Over")

        def create_game_over_text_and_animation():
            animation = turtle.Turtle()
            animation.penup()
            animation.goto(0, 0)
            animation.shape("assets/gameover.gif")

            game_over_turtle = turtle.Turtle()
            game_over_turtle.penup()
            game_over_turtle.goto(0, -self.bounding_box_limit["height"] + 50)
            game_over_turtle.color("white")
            game_over_turtle.write(
                "Press Enter to Restart or Q to Quit",
                align="center",
                font=("Press Start 2P", 24, "normal"),
            )
            game_over_turtle.hideturtle()

            self.screen.listen()

            self.screen.onkeypress(lambda: callback(), "Return")
            self.screen.onkeypress(lambda: self.screen.bye(), "q")

        def create_final_score_text():
            final_score_turtle = turtle.Turtle()
            final_score_turtle.penup()
            final_score_turtle.goto(0, -self.bounding_box_limit["height"] + 110)
            final_score_turtle.color("white")
            final_score_turtle.write(
                f"Final Score: {score}",
                align="center",
                font=("Press Start 2P", 24, "normal"),
            )
            final_score_turtle.hideturtle()

        create_game_over_text_and_animation()
        create_final_score_text()

        self.screen.update()

    def draw_border(self):
        """Draws the border of the game screen."""
        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.color("#22493b")
        self.border.penup()
        self.border.goto(
            self.bounding_box_limit["width"], self.bounding_box_limit["height"]
        )
        self.border.pendown()
        self.border.pensize(5)

        # Draw the square border
        for i in range(4):
            self.border.right(90)
            self.border.forward(self.bounding_box_limit["width"] * 2)
