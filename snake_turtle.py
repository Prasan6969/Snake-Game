import turtle
import time
import random

#declaring constants and managing the width and height 
WIDTH,HEIGHT = 700,600
MOVE_DISTANCE = 17
DELAY = 0.1

#creating the screen for the game
wn=turtle.Screen()
wn.setup(WIDTH,HEIGHT)
wn.bgcolor("#f2efe7")
wn.title("Snake and Turtle")
wn.tracer(0)#this is used to turn off any automatic updates

#shaping the game character
head=turtle.Turtle()
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#creating and shaping food 
food=turtle.Turtle()
food.shape("circle")
food.color("red") 
food.penup()
segments=[]


max_cell_x = (WIDTH//2 - MOVE_DISTANCE) // MOVE_DISTANCE
max_cell_y = (HEIGHT//2 - MOVE_DISTANCE) // MOVE_DISTANCE
def food_spawn():#justifying the function to make sure food spawns in correct position
    ranx=random.randint(-max_cell_x, max_cell_x)
    rany=random.randint(-max_cell_y, max_cell_y)
    food_x = ranx * MOVE_DISTANCE
    food_y= rany * MOVE_DISTANCE
    food.goto(food_x, food_y)

food_spawn()

# defining necessary functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# preventing the keys from reversing
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + MOVE_DISTANCE)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y - MOVE_DISTANCE)
    
    if head.direction=="right":
        x=head.xcor()
        head.setx(x + MOVE_DISTANCE)
    
    if head.direction=="left":
        x=head.xcor()
        head.setx(x - MOVE_DISTANCE)
        
#key bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")




while True:
    wn.update()
    
    before_x=head.xcor()#it helps to restore the original position of head
    before_y=head.ycor()
    
    move()
    if head.distance(food)< MOVE_DISTANCE:
        food_spawn()
    #creating segments for snake so that it can be added and make the snake bigger when eating the turtle
        new_segment=turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments)-1,0,-1):
        new_x,new_y=segments[i-1].pos()
        segments[i].goto(new_x,new_y)
    
    if len(segments)>0:
        segments[0].goto(before_x, before_y)
        
    time.sleep(DELAY)






