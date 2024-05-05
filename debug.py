class Debug():
    def __init__(self, snake, screen, food) -> None:
        self.snake = snake
        self.screen = screen
        self.food = food
    
    def snake_pos(self):
        return f'Snake pos {self.snake.pos()} at heading {self.snake.heading()}'
    
    def snake_body(self):
        return f'Snake body has length {len(self.snake.body)}'

    def food_pos(self):
        return f'Food pos {self.snake.food.pos()}'
    
    def food_distance(self):
        return f'Food distance {self.snake.food.distance(self.snake.pos())}'