# Customizing the Game's Appearance

This document outlines how to modify various visual aspects of the Snake game.

## 1. Snake Movement Speed

The `FOWARD_AMOUNT` variable controls how many pixels the snake moves forward in each step.

- **File:** `SnakeGame.py`
- **Variable:** `self.FOWARD_AMOUNT`

To change the speed, modify the value of `self.FOWARD_AMOUNT`. A higher value means faster movement.

```python
# SnakeGame.py

class Game_Engine:
    def __init__(self, DEBUG=False):
        # ...
        self.FOWARD_AMOUNT = 20  # Adjust this value for desired speed
        # ...
```

## 2. Snake Head Images

The snake's head uses different images based on its heading direction.

- **Files:** `snake.py`, `screen.py`
- **Image Assets:** `snake_assets/snake_head_0.gif`, `snake_assets/snake_head_90.gif`, `snake_assets/snake_head_180.gif`, `snake_assets/snake_head_270.gif`

To change the snake head's appearance:
1. **Update `snake.py`:** In the `Snake` class, the `shape()` method in `__init__` and `set_snake_properties` sets the initial head image.
   ```python
   # snake.py

   class Snake(turtle.Turtle):
       def __init__(self):
           # ...
           self.shape('snake_assets/your_new_head_image_0.gif') # Update this
           # ...

       def set_snake_properties(self):
           # ...
           self.shape('snake_assets/your_new_head_image_0.gif') # Update this
           # ...
   ```
2. **Update `game_controls.py`:** The `go_snake_up`, `go_snake_down`, `go_snake_right`, and `go_snake_left` methods update the snake's head image based on its direction.
   ```python
   # game_controls.py

   class Game_Controller():
       # ...
       def go_snake_up(self):
           # ...
           self.snake.shape('snake_assets/your_new_head_image_90.gif') # Update this
           # ...

       def go_snake_down(self):
           # ...
           self.snake.shape('snake_assets/your_new_head_image_270.gif') # Update this
           # ...

       def go_snake_right(self):
           # ...
           self.snake.shape('snake_assets/your_new_head_image_0.gif') # Update this
           # ...

       def go_snake_left(self):
           # ...
           self.snake.shape('snake_assets/your_new_head_image_180.gif') # Update this
           # ...
   ```
3. **Register Shapes in `screen.py`:** Ensure your new image files are registered with the `turtle` screen.
   ```python
   # screen.py

   class Game_Screen():
       def __init__(self):
           # ...
           self.screen.register_shape('snake_assets/your_new_head_image_0.gif')
           self.screen.register_shape('snake_assets/your_new_head_image_90.gif')
           self.screen.register_shape('snake_assets/your_new_head_image_180.gif')
           self.screen.register_shape('snake_assets/your_new_head_image_270.gif')
           # ...
   ```
   Make sure to place your new `.gif` image files in the `snake_assets/` directory.

## 3. Food Image

The food's appearance is determined by a GIF image.

- **File:** `screen.py`
- **Image Asset:** `apple.gif`

To change the food's appearance:
1. **Update `screen.py`:** In the `Game_Screen` class, modify the `register_shape()` call for the food.
   ```python
   # screen.py

   class Game_Screen():
       def __init__(self):
           # ...
           self.screen.register_shape('your_new_food_image.gif') # Update this
           # ...
   ```
   Make sure to place your new `.gif` image file in the root directory of the project.

## 4. Screen Background Color and Size

You can customize the game window's background color and dimensions.

- **File:** `screen.py`

To change the screen properties:
1. **Update `screen.py`:** In the `Game_Screen` class, modify `bgcolor()` and `screensize()`.
   ```python
   # screen.py

   class Game_Screen():
       def __init__(self):
           # ...
           self.screen.bgcolor('black') # Change to your desired color (e.g., 'blue', '#RRGGBB')
           self.screen.screensize(800, 600) # Change width and height
           # ...
   ```

## 5. Snake Body Segment Appearance

The snake's body segments are simple circles.

- **File:** `snake.py`

To change the body segment's appearance:
1. **Update `snake.py`:** In the `increase_snake_lenght()` method of the `Snake` class, you can modify the `shape()`, `shapesize()`, and `color()` of the new segments.
   ```python
   # snake.py

   class Snake(turtle.Turtle):
       # ...
       def increase_snake_lenght(self):
           # ...
           new_segment.shape('square') # Change to 'square', 'triangle', 'circle', etc.
           new_segment.shapesize(1.2, 1.2) # Adjust size (stretch_wid, stretch_len)
           new_segment.color('gray') # Change to your desired color
           # ...
   ```
   You can also use `register_shape` in `screen.py` and then use `new_segment.shape('your_custom_body_segment.gif')` if you want to use an image for the body segments.


## 6. Game FPS
- **file** `SnakeGame.py`

To change the game FPS logic go to the file:
- 1 Modify the `RENDER_FPS` constant to wished FPS:
```python
        # FPS settings:
        self.RENDER_FPS = 60  # Change this constant value
        
        self.frame_counter = 0
        
        self.render_per_logic = self.RENDER_FPS / self.LOGIC_FPS
```
## 7 Game velocity 
- **file** `SnakeGame.py`

To set the velocity/difficulty of the game:

- 1 Modify the `LOGIC_FPS` constant, as a result, a higher value means a higher velocity/difficulty on game
```python
    self.LOGIC_FPS = 10  # Logic per second / How many times the game logic is processed per second example move snake
```

## 8 Initial Snake Length
- **file** `snake.py`

To change the initial snake length, change the following constant in the snake Class:
```python
class Snake(turtle.Turtle):
    def __init__():
        self.INITIAL_LENGTH = 3 # the amount you wish snake starts with
        
```

Btw, the function that start the `INITIAL_LENGTH` is the `create_snake_body`:
```python
def create_snake_body(self):
    """Creates the initial body of the snake."""
    # To initial snake body segments
    for _ in range(self.INITIAL_LENGTH):
        self.increase_snake_length()
```

## 9 Snake blink green on eat
- **File** ``SnakeGame.py`

```python
    self.FLASH_DURATION = 0.5 # Duration of blink


    def  trigger_flash(self):
        # called when snake colid with food
    
    def handle_flash_effect(self):
        # handle if actual time is within the interval to the end of blink
```
- **Attention** `trigger_flash` add a new property to the game instance, **`flash_end_time`** that is the time in ms when the blink
effect is supposed to end, therefore, don´t try to manipulate or check this property in other parts of code, or if you need to, make sure you do it safely using `hasattr`