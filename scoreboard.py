from turtle import Turtle

ALIGN = 'center'

FONT = ('Arial', 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0, 270)
        self.color('green')
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.write(f'El puntaje es: {self.score}', font=FONT, align=ALIGN)
    
    def increased_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,.0)
        self.write(f'Juego terminado \nTu puntaje es: {self.score}', font=FONT, align=ALIGN)
