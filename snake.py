from turtle import Turtle,Screen

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)


    def add_segments(self,position):       
        segment=Turtle(shape="square")
        segment.color("white")
        segment.pu()
        segment.goto(position)
        self.segments.append(segment)


    def extend_snake(self):
        self.add_segments(self.segments[-1].position())    


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()    

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):   #range(start,stop,step)
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)



    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)   



    def down(self):
        if self.segments[0].heading() != UP:
        
            self.segments[0].setheading(DOWN) 




    def right(self):
        if self.segments[0].heading() != LEFT:
       
            self.segments[0].setheading(RIGHT) 



    def left(self):
        if self.segments[0].heading() != RIGHT:
       
            self.segments[0].setheading(LEFT) 



