import random
from snake import Snake
from food import Food
from score import Score
from screen import Game_Screen
from game_controls import Game_Controller


class Game_Engine:
    """
    The main engine for the Snake game.

    This class is responsible for initializing and running the game,
    managing the game state, and handling game logic such as collisions,
    scoring, and player input.
    """

    def __init__(self, DEBUG=False):
        """
        Initializes the Game_Engine.

        Args:
            DEBUG (bool, optional): Whether to run the game in debug mode.
            Defaults to False.
        """

        self.DEBUG = DEBUG

        self.FOWARD_AMOUNT = 20

        # FPS settings:
        self.RENDER_FPS = 60  # Frames per second
        self.LOGIC_FPS = 10  # Logic per second / How many times the game logic is processed per second example move snake
        self.frame_counter = 0

        self.render_per_logic = self.RENDER_FPS / self.LOGIC_FPS

        # Game Screen
        self.game_screen = Game_Screen()
        self.screen = self.game_screen.screen

        self.show_start_screen()

    def show_start_screen(self):
        self.game_screen.show_start_screen(self.start_game)

    def start_game(self):
        """Initializes the game state and starts the game loop."""
        self.screen.clear()
        self.screen.tracer(0)
        self.game_screen.draw_border()

        self.is_game_on = True

        self.screen.title("Snake Game")
        self.screen.bgcolor("#1fdb83")

        # Create Snake
        self.snake = Snake()

        # Food
        self.food = Food()
        self.positionate_food()

        # Score
        self.score = Score()

        self.score.write_score()

        self.game_controls = Game_Controller(self.screen, self.snake)
        self.keys_list = self.game_controls.keys_pressed

        self.is_game_on = True

        self.game_loop()

    def increase_player_point(self):
        """Increases the player's score by 1 and updates the score display."""
        self.score.increase_score()
        self.score.update_score()

    def positionate_food(self):
        """Places the food at a random position on the screen."""
        new_x = random.randint(
            round(self.game_screen.bounding_box_limit["width"] * -1),
            round(self.game_screen.bounding_box_limit["width"]),
        )
        new_y = random.randint(
            round(self.game_screen.bounding_box_limit["height"] * -1),
            round(self.game_screen.bounding_box_limit["height"]),
        )
        self.food.goto(new_x, new_y)

        if self.DEBUG:
            print(f"Food position: {self.food.position()}")

    def set_game_over(self):
        """Ends the game and displays the game over screen."""

        self.screen.bgcolor("black")
        self.screen.title("Game Over")

        self.score.save_high_score()

        # Hide the snake and food
        self.snake.hideturtle()
        self.food.hideturtle()

        for segment in self.snake.snake_body:
            segment.hideturtle()

        self.screen.clear()

        # TODO: Show game over screen with score and high score
        self.game_screen.show_game_over_screen(score=self.score.score, callback=lambda: self.start_game())

        self.is_game_on = False

    def check_colision_with_food(self):
        """Checks for collision between the snake and the food."""
        if self.snake.distance(self.food) < 15:
            self.increase_player_point()
            self.positionate_food()
            self.snake.increase_snake_length()

    def check_colision_with_border(self):
        """Checks for collision between the snake and the screen border."""
        if (
            self.snake.xcor() > self.game_screen.bounding_box_limit["width"]
            or self.snake.xcor() < -self.game_screen.bounding_box_limit["width"]
        ):
            self.set_game_over()
        elif (
            self.snake.ycor() > self.game_screen.bounding_box_limit["height"]
            or self.snake.ycor() < -self.game_screen.bounding_box_limit["height"]
        ):
            self.set_game_over()

    def check_colision_with_tail(self):
        """Checks for collision between the snake and its own tail."""
        for segment in self.snake.snake_body[1:]:
            if round(self.snake.distance(segment)) < self.FOWARD_AMOUNT:
                if self.DEBUG:
                    print(
                        f"Collision with tail at position: {segment.position()}, distance: {self.snake.distance(segment)}, snake position: {self.snake.position()}"
                    )
                self.set_game_over()

    def check_all_colisions(self) -> None:
        """Checks for all possible collisions in the game."""
        self.check_colision_with_tail()
        self.check_colision_with_border()
        self.check_colision_with_food()

    def move_snake(self):
        """Moves the snake forward and checks for collisions."""

        for segment in range(len(self.snake.snake_body) - 1, 0, -1):
            new_x = self.snake.snake_body[segment - 1].xcor()
            new_y = self.snake.snake_body[segment - 1].ycor()
            self.snake.snake_body[segment].goto(new_x, new_y)

        # move the head of snake
        self.snake.forward(self.FOWARD_AMOUNT)

    def game_loop(self):
        """Runs the game loop updating the screen and checking all logic."""

        self.frame_counter += 1
        self.screen.update()

        if self.frame_counter % self.render_per_logic == 0:
            if self.keys_list:
                self.keys_list.pop(0)
            self.move_snake()
            self.check_all_colisions()

        if self.is_game_on:
            self.screen.ontimer(
                self.game_loop,
                round(1000 / 120),  # 120 FPS
            )


a = Game_Engine(DEBUG=True)


a.screen.mainloop()
