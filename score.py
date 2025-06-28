import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('white')
        
        self.score = 0
        self.high_score = self.get_high_score()
        
        self.write_score()
    
    def write_score(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def update_score(self):
        self.clear()
        self.check_score_greater_than_high_score()
        self.write_score()

    def increase_score(self):
        self.score += 1
        
    def check_score_greater_than_high_score(self):
        if self.score > self.high_score:
            self.color('red')
            return True
            
    def save_high_score(self):
        if self.check_score_greater_than_high_score():
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
    
    def get_high_score(self):
        try:
            with open('high_score.txt', mode='r') as file:
                self.high_score = int(file.read())
                
        except FileNotFoundError:
            print('High score file not found. Setting high score to 0.')
            return 0
        return self.high_score
    