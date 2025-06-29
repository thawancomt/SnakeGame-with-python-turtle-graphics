import random
import time
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
        self.RENDER_FPS = 60  # Frames per second for rendering
        self.LOGIC_FPS = 15   # Logic updates per second (snake movement speed)
        self.frame_counter = 0

        self.render_per_logic = self.RENDER_FPS / self.LOGIC_FPS

        # --- New attributes for non-blocking flash effect ---
        self.is_flashing = False
        self.flash_end_time = 0
        self.FLASH_DURATION = 0.5  # Flash for 0.5 seconds

        # Game Screen
        self.game_screen = Game_Screen()
        self.screen = self.game_screen.screen

        # Display the start screen and wait for user input to begin the game
        self.show_start_screen()

    # --- Game State Management ---
    def show_start_screen(self):
        """Displays the initial start screen and sets up input for starting the game."""
        self.game_screen.show_start_screen(self.start_game)

    def start_game(self):
        """Initializes the game state and starts the main game loop."""
        self.screen.clear()
        self.screen.tracer(0)  # Turn off automatic screen updates
        self.game_screen.draw_border()

        self.is_game_on = True
        self.is_flashing = False # Reset flashing state on new game

        self.screen.title("Snake Game")
        self.screen.bgcolor("#1a1a1a")

        # Initialize game entities
        self.snake = Snake()
        self.food = Food()
        self.positionate_food()
        self.score = Score()
        self.score.write_score()
        self.game_controls = Game_Controller(self.screen, self.snake)
        self.keys_list = self.game_controls.keys_pressed

        # Begin the game loop
        self.game_loop()

    def set_game_over(self):
        """Ends the game, saves the high score, and displays the game over screen."""
        self.is_game_on = False # Stop the game loop immediately
        self.screen.bgcolor("black")
        self.screen.title("Game Over")

        self.score.save_high_score()

        # Hide game entities
        self.snake.hideturtle()
        self.food.hideturtle()
        for segment in self.snake.snake_body:
            segment.hideturtle()

        self.screen.clear()

        # Show game over screen with option to restart
        self.game_screen.show_game_over_screen(
            score=self.score.score, callback=lambda: self.start_game()
        )

    # --- Game Logic ---
    def increase_player_point(self):
        """Increases the player's score and updates the display."""
        self.score.increase_score()
        self.score.update_score()

    def positionate_food(self):
        """Places the food at a random position within the game boundaries."""
        # This ensures food doesn't spawn on a snake segment
        while True:
            new_x = random.randrange(
                int(self.game_screen.bounding_box_limit["width"] * -1) + 20,
                int(self.game_screen.bounding_box_limit["width"]) - 20,
                self.FOWARD_AMOUNT
            )
            new_y = random.randrange(
                int(self.game_screen.bounding_box_limit["height"] * -1) + 20,
                int(self.game_screen.bounding_box_limit["height"]) - 20,
                self.FOWARD_AMOUNT
            )
            self.food.goto(new_x, new_y)

            # Check if the food position is on the snake
            is_on_snake = False
            for segment in self.snake.snake_body:
                if self.food.distance(segment) < 10:
                    is_on_snake = True
                    break
            
            if not is_on_snake:
                break # Found a valid position

        if self.DEBUG:
            print(f"Food position: {self.food.position()}")

    # --- Collision Detection ---
    def check_colision_with_food(self):
        """Checks for collision between the snake's head and the food."""
        if self.snake.distance(self.food) < 15:
            self.increase_player_point()
            self.positionate_food()
            self.snake.increase_snake_length()
            # --- Trigger the flash effect instead of blocking ---
            self.trigger_flash()

    def check_colision_with_border(self):
        """Checks for collision between the snake's head and the screen borders."""
        head = self.snake
        if (
            head.xcor() >= self.game_screen.bounding_box_limit["width"]
            or head.xcor() <= -self.game_screen.bounding_box_limit["width"]
            or head.ycor() >= self.game_screen.bounding_box_limit["height"]
            or head.ycor() <= -self.game_screen.bounding_box_limit["height"]
        ):
            self.set_game_over()

    def check_colision_with_tail(self):
        """Checks for collision between the snake's head and its own body segments."""
        for segment in self.snake.snake_body[1:]:
            if self.snake.distance(segment) < 10:
                if self.DEBUG:
                    print(
                        f"Collision with tail at position: {segment.position()}, distance: {self.snake.distance(segment)}, snake position: {self.snake.position()}"
                    )
                self.set_game_over()

    def check_all_colisions(self) -> None:
        """Orchestrates all collision checks (tail, border, food)."""
        # Checks are ordered by importance. Tail/Border collision ends the game.
        self.check_colision_with_tail()
        # A guard to prevent further checks if game is over
        if not self.is_game_on: return
        self.check_colision_with_border()
        if not self.is_game_on: return
        self.check_colision_with_food()


    # --- Snake Movement & Effects ---
    def move_snake(self):
        """Moves the snake forward by updating the positions of its segments."""
        for segment_num in range(len(self.snake.snake_body) - 1, 0, -1):
            new_x = self.snake.snake_body[segment_num - 1].xcor()
            new_y = self.snake.snake_body[segment_num - 1].ycor()
            self.snake.snake_body[segment_num].goto(new_x, new_y)

        # Move the head of the snake
        self.snake.forward(self.FOWARD_AMOUNT)

    def  trigger_flash(self):
        """Activates the flashing state and sets the end time."""
        self.is_flashing = True
        self.flash_end_time = time.time() + self.FLASH_DURATION
        # Set the color immediately on trigger
        for segment in self.snake.snake_body:
            segment.color("#1bd060") # Bright green

    def handle_flash_effect(self):
        """Manages the snake's color during the flash effect.
        This runs every frame, not just on logic ticks."""
        if self.is_flashing:
            # Check if the flash duration has passed
            if time.time() > self.flash_end_time:
                self.is_flashing = False
                # Reset color to normal
                for segment in self.snake.snake_body:
                    segment.color("white")
                    
            else:
                 # Ensure color stays green during the flash
                for segment in self.snake.snake_body:
                    segment.color("#1bd060")


    # --- Game Loop ---
    def game_loop(self):
        """
        The main game loop, responsible for updating the screen, processing game logic,
        and handling frame rate.
        """
        # This check is crucial. If game is over, the loop stops calling itself.
        if not self.is_game_on:
            return

        self.frame_counter += 1

        # --- Logic that runs every RENDER frame ---
        self.handle_flash_effect() # Manage the visual effect smoothly

        # --- Logic that runs at a slower, controlled rate (LOGIC_FPS) ---
        if self.frame_counter % self.render_per_logic == 0:
            if self.keys_list:
                # Process only the most recent key press to avoid strange turns
                self.keys_list.pop(0)
            self.move_snake()
            self.check_all_colisions()

        # Update the screen to show all changes made in this frame
        self.screen.update()

        # Schedule the next iteration of the game loop
        self.screen.ontimer(
            self.game_loop,
            round(1000 / self.RENDER_FPS)
        )


# --- Game Initialization ---
if __name__ == "__main__":
    # Create an instance of the Game_Engine to start the game
    game = Game_Engine(DEBUG=True)
    # Keep the turtle graphics window open
    game.screen.mainloop()
