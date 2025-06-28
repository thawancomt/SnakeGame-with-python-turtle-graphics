import json
import turtle

class Score(turtle.Turtle):
    """
    A class to manage the score in the Snake game.
    
    This class inherits from the turtle.Turtle class and is responsible
    for displaying and updating the score, as well as tracking the high score.
    """
    def __init__(self):
        """Initializes the Score object."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('white')
        
        self.score = 0
        self.high_score = self.get_high_score()
        
        
    
    def write_score(self):
        """Writes the current score to the screen."""
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def update_score(self):
        """Updates the score display."""
        self.clear()
        self.check_score_greater_than_high_score()
        self.write_score()

    def increase_score(self):
        """Increases the score by 1."""
        self.score += 1
        
    def check_score_greater_than_high_score(self):
        """Checks if the current score is greater than the high score."""
        if self.score > self.high_score:
            self.color('red')
            return True
            
    def save_high_score(self):
        """Saves the high score to a file."""
        if self.check_score_greater_than_high_score():
            self.high_score = self.score
            with open('high_score.json', mode='w') as file:
                file.write(
                    json.dumps({
                        "high_score": self.high_score,
                    }, indent=4)
                )
    
    def get_high_score(self):
        """Gets the high score from a file."""
        try:
            with open('high_score.json', mode='r') as file:
                data = json.load(file)
                return data.get('high_score', 0)
        except FileNotFoundError:
            print('High score file not found. Setting high score to 0.')
            return 0
        return self.high_score
    