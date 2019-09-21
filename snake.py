#BRIANS COMPUTER IS NUMBER 4
import random
import turtle as t
game_start = False

t.bgcolor("yellow")
#snake implementation
snake = t.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(0)  
snake.penup()
snake.hideturtle()


#apple implementation
snack = t.Turtle()
snack.shape("turtle")
snack.color("red")
snack.speed(0)
snack.penup()
snack.hideturtle()

#todo movesnake, controldirection w/keyinputs
#blit snake in random window spaces
#blit the food
#Menu stuff
game_menu = t.Turtle()
game_menu.write("Press SPACE key to play",align="center", \
                                font=("Arial",17,"normal"))
game_menu.hideturtle()
#score implemenation
turtle_score=t.Turtle()
turtle_score.hideturtle()
turtle_score.speed(0)

def WALL():
    #if nakse hits border then it dies and return true
    L_WALL = -(t.window_width()/2)
    R_WALL = (t.window_width()/2)
    T_WALL = (t.window_height()/2)
    B_WALL = -(t.window_height()/2)
#where snake
    (x,y)= snake.pos()
    #return tru IF X IS OUTSIDE OF BORDER SCOPE
    outside = \
            x < L_WALL or\
            x > R_WALL or\
            x > T_WALL or\
            x < B_WALL

    return outside

def END():
    #end the game show scoresave to hi score
    t.penup()
    t.hideturtle()
    t.write("git gud NOOB",align="center",font=("Arial",18,"normal"))
def SCORES(game_score):
    #update scores
    turtle_score.clear()
    turtle_score.penup()
    x = (t.window_width() / 2)-53
    y = (t.window_height() / 2)-42

    turtle_score.setpos(x,y)
    turtle_score.write(str(game_score),align="right",font=("Arial",19,"italic"))
def BLITFOOD():
    #make snack on the screen for snak to eat
    snack.setpos(x=random.randint(-200,200),y=random.randint(-200,200))
def UP():
    if snake.heading() == 0 or snake.heading()==180:
        snake.setheading(90)
def DOWN():
    if snake.heading() ==0 or snake.heading()==180:
        snake.setheading(270)
def RIGHT():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(0)
def LEFT():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(180)
def START():
    global game_start
    if game_start:
        return

    game_start = True

    game_score = 0

    game_menu.clear()
    snake_speed = 1
    snake_size = 3
    snake.shapesize(1,snake_size,1)
    snake.showturtle()
    snack.showturtle()
    SCORES(game_score)

    BLITFOOD()
    while True:
        snake.forward(snake_speed)
        if snake.distance(snack) < 30:#if snake in 30px distance of snak eat snak 
            BLITFOOD()                #food somewhere else
            snake_size=snake_size+1   # make snake bigger
            snake.shapesize(1,snake_size,1)
            snake_speed = snake_speed + 1
            game_score = game_score+10000
            SCORES(game_score)
        if WALL():
            END()
            #DIE!!!
            break
        #kill the loop

t.onkey(START,"space")
t.onkey(UP,"Up")
t.onkey(DOWN,"Down")
t.onkey(RIGHT,"Right")
t.onkey(LEFT,"Left")
    
t.listen()
t.mainloop



