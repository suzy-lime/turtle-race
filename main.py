from turtle import Turtle, Screen
import random

# SCREEN
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Choose your racer", prompt="Which turtle will win the race. Pick a color: ")

# TURTLES
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=(-125 + (50 * turtle_index)))
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost. The {winning_color} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
