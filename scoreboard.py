from turtle import Turtle

ALIGNMENT ="center"
FONT=('Bahnschrift', 20, 'normal')





class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            self.highest_score=int(data.read())
    
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)


    def update_score(self):

        self.write(arg= f"score : {self.score} Highest score: {self.highest_score}",move=False,align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score=0   
        self.update_score() 


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg= f"GAME OVER!😢 \nYour score is {self.score}",move=False,align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.update_score()