import turtle
import random
import time
drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("My Drawing Board")

score = 0
start_time = time.time()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
time0=turtle.Turtle()
time0.hideturtle()
time0.penup()
top_y = drawing_board.window_height()/2-20
time0.goto(0, top_y)
pen.goto(0, top_y+30)

def change_color(x,y):
    turtle_obj.color("Black")
turtle_obj = turtle.Turtle()
turtle_obj.shape("turtle")
turtle_obj.onclick(change_color)
turtle_obj.shapesize(3)
turtle_obj.penup()
turtle_obj.speed(0)

def update_score():
    pen.clear()
    pen.write(f"Score : {score}",align="center", font=("Arial", 16, "normal"))
def get_mouse_click_coor(x, y):
    global score
    if turtle_obj.distance(x, y)<40:
        score += 1
        update_score()
        print("Skor :",score)


def move_turtle():
    elapsed_time = time.time() - start_time
    if elapsed_time <30:
        a = random.randint(-500, 500)
        b = random.randint(-500, 500)
        turtle_obj.goto(a,b)
        update_score()
        drawing_board.ontimer(move_turtle, 500)
    else:
        pen.clear()
        pen.goto(0,0)
        pen.write(f"Game Over!\nFinal Score : {score}",align="center", font=("Arial", 25, "bold"))
    time0.clear()
    time0.write((round(time.time() - start_time)), align="center", font=("Arial", 20, "bold"))
move_turtle()
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

turtle.done()

