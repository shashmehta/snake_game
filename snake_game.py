
import turtle
import time
import random
import pickle

delay = 0.11

# score

score = 0
high_score = pickle.load(open("high_scores", "rb"))




# set up window

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("Cyan")
win.setup(width=600, height=600)
win.tracer(0)

# snake head

hd = turtle.Turtle()
hd.speed(0)
hd.shape("square")
hd.color("Dark Green")
hd.penup()
hd.goto(0, 0)
hd.direction = "stop"

# food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0, 50)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("triangle")
pen.color("Black")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
high_score = pickle.load(open("high_scores", "rb"))

pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "normal"))





# Functions

def restart():
    time.sleep(1)
    hd.goto(0, 0)
    food.goto(0, 50)
    hd.direction = "stop"


    # hide segments when game restarts

    for segment in segments:
        segment.goto(900000, 900000)

    # clear segments list

    segments.clear()

    score = 0
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "normal"))





def up():
    if hd.direction != "down":
        hd.direction = "up"
def down():
    if hd.direction != "up":
        hd.direction = "down"
def left():
    if hd.direction != "right":
        hd.direction = "left"
def right():
    if hd.direction != "left":
        hd.direction = "right"


def move():

    if hd.direction == "up":
        y = hd.ycor()
        hd.sety(y + 20)
    if hd.direction == "down":
        y = hd.ycor()
        hd.sety(y - 20)
    if hd.direction == "left":
        x = hd.xcor()
        hd.setx(x - 20)
    if hd.direction == "right":
        x = hd.xcor()
        hd.setx(x + 20)


# key presses

win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")


# main game loop
while True:
    win.update()

    # check if touching border

    if hd.xcor() > 290 or hd.xcor() < -290 or hd.ycor() > 290 or hd.ycor() < -290:

        restart()
        score = 0

    if hd.distance(food) < 20:
        # I am touching food, let me move it.
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # I ate food, adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("Lime Green")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        # increase score
        score += 10

        if score > high_score:
            high_score = score

            pickle.dump(high_score, open("high_scores", "wb"))

            high_score = pickle.load(open("high_scores", "rb"))

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "normal"))



        # move back tail to front
    for index in range(len(segments ) -1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = hd.xcor()
        y = hd.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(hd) < 20:

            restart()
            score = 0


    time.sleep(delay)


win.mainloop()
