# Game Flow and Architecture

This document explains the overall flow of the Snake game, detailing how different classes interact and the order in which key functions are called.

## 1. Game Initiation (`SnakeGame.py`)

The game starts by creating an instance of the `Game_Engine` class in `SnakeGame.py`:

```python
a = Game_Engine(DEBUG=True)
```

-   **`Game_Engine.__init__(self, DEBUG=False)`:**
    -   Initializes game settings like `FOWARD_AMOUNT`, `RENDER_FPS`, `LOGIC_FPS`.
    -   Creates an instance of `Game_Screen`:
        ```python
        self.game_screen = Game_Screen()
        self.screen = self.game_screen.screen
        ```
    -   Calls `self.show_start_screen()` to display the initial game screen.

-   **`Game_Screen.__init__(self)` (in `screen.py`):**
    -   Sets up the `turtle` screen properties (title, tracer, background, size).
    -   Registers custom shapes for the snake head and food (`apple.gif`, `snake_head_*.gif`).

-   **`Game_Engine.show_start_screen(self)`:**
    -   Calls `self.game_screen.show_start_screen(self.start_game)`.

-   **`Game_Screen.show_start_screen(self, callback)` (in `screen.py`):**
    -   Configures the start screen's appearance (background color, title).
    -   Creates and displays instructions and high score text using `turtle.Turtle` objects.
    -   Sets up event listeners for 'Enter' (to call the `callback`, which is `Game_Engine.start_game`) and 'q' (to quit).

-   **`a.screen.mainloop()`:**
    -   This line keeps the `turtle` graphics window open and responsive to events until it's manually closed.

## 2. Starting the Game (`Game_Engine.start_game`)

When the user presses 'Enter' on the start screen, `Game_Engine.start_game()` is called:

-   **`Game_Engine.start_game(self)`:**
    -   Clears the screen and resets `tracer`.
    -   Calls `self.game_screen.draw_border()` to draw the game boundaries.
    -   Sets `self.is_game_on = True`.
    -   Initializes game entities:
        -   `self.snake = Snake()`: Creates the snake object.
        -   `self.food = Food()`: Creates the food object.
        -   `self.positionate_food()`: Places the food randomly.
        -   `self.score = Score()`: Initializes the score tracker.
        -   `self.score.write_score()`: Displays the initial score.
        -   `self.game_controls = Game_Controller(self.screen, self.snake)`: Sets up keyboard controls.
    -   Calls `self.game_loop()` to begin the main game loop.

## 3. Game Loop (`Game_Engine.game_loop`)

The `game_loop` function is the heart of the game, called repeatedly by `screen.ontimer`.

-   **`Game_Engine.game_loop(self)`:**
    -   Increments `self.frame_counter`.
    -   `self.screen.update()`: Refreshes the screen to show changes.
    -   **Logic Update (conditional):** `if self.frame_counter % self.render_per_logic == 0:`
        -   This condition ensures game logic (movement, collision) is processed at `LOGIC_FPS` while rendering happens at `RENDER_FPS`.
        -   `self.keys_list.pop(0)`: Processes one pending key press.
        -   `self.move_snake()`: Updates the snake's position.
        -   `self.check_all_colisions()`: Checks for all types of collisions.
    -   **Recursive Call:** `self.screen.ontimer(self.game_loop, round(1000 / self.RENDER_FPS))`:
        -   Schedules the next call to `game_loop` based on the `RENDER_FPS`.

## 4. Key Class Interactions

-   **`Snake` (in `snake.py`):**
    -   Manages the snake's body segments, movement (`forward`, `setheading`), and appearance.
    -   `increase_snake_length()`: Adds new segments to the snake.

-   **`Food` (in `food.py`):**
    -   Represents the food item.
    -   `goto()`: Moves the food to a new position.

-   **`Score` (in `score.py`):**
    -   Tracks the player's score and high score.
    -   `increase_score()`, `update_score()`, `save_high_score()`, `get_high_score()`.

-   **`Game_Screen` (in `screen.py`):**
    -   Manages the `turtle` screen, background, and border.
    -   `show_start_screen()`, `draw_border()`, `show_game_over_screen()`.

-   **`Game_Controller` (in `game_controls.py`):**
    -   Handles user input (arrow keys).
    -   Calls `snake.setheading()` and `snake.shape()` to change the snake's direction and appearance.

## 5. Game Over (`Game_Engine.set_game_over`)

When a collision occurs, `Game_Engine.set_game_over()` is called:

-   **`Game_Engine.set_game_over(self)`:**
    -   Changes screen background and title.
    -   `self.score.save_high_score()`: Saves the current score if it's a new high score.
    -   Hides the snake and food.
    -   Clears the screen.
    -   Calls `self.game_screen.show_game_over_screen(score=self.score.score, callback=lambda: self.start_game())` to display the game over screen with a restart option.
    -   Sets `self.is_game_on = False` to stop the game loop.
