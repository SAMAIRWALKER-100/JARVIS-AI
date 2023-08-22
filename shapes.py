import turtle
from time import sleep as wait
from ai import AI

JARVIS = AI()

class SP():
    def triangle():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(3):
            my_turtle1.forward(200)
            my_turtle1.left(120)
        turtle.exitonclick()

    def square():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(4):
            my_turtle1.forward(200)
            my_turtle1.left(90)
        turtle.exitonclick()

    def rectangle():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        my_turtle1.forward(300)
        my_turtle1.left(90)
        my_turtle1.forward(200)
        my_turtle1.left(90)
        my_turtle1.forward(300)
        my_turtle1.left(90)
        my_turtle1.forward(200)
        my_turtle1.left(90)
        turtle.exitonclick()

    def pentagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(5):
            my_turtle1.forward(200)
            my_turtle1.left(72)
        turtle.exitonclick()

    def hexagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(6):
            my_turtle1.forward(200)
            my_turtle1.left(60)
        turtle.exitonclick()

    def heptagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(7):
            my_turtle1.forward(100)
            my_turtle1.left(51.43)
        turtle.exitonclick()
    
    def octagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(8):
            my_turtle1.forward(100)
            my_turtle1.left(45)
        turtle.exitonclick()

    def nonagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(9):
            my_turtle1.forward(100)
            my_turtle1.left(40)
        turtle.exitonclick()

    def decagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(10):
            my_turtle1.forward(100)
            my_turtle1.left(36)
        turtle.exitonclick()

    def hendecagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(11):
            my_turtle1.forward(100)
            my_turtle1.left(32.7)
        turtle.exitonclick()
    
    def dodecagon():
        my_turtle1 = turtle.Turtle()
        my_turtle1.shape("turtle")
        my_turtle1.color("green")
        wait(0.05)
        for i in range(12):
            my_turtle1.forward(100)
            my_turtle1.left(30)
        turtle.exitonclick()
    wait(1.5)
    JARVIS.say("What Shape Would You Like Me to Draw")
    ask = str
    ask = JARVIS.listen()
    print(ask)
    
    if ask == "a square":
        square()
    elif ask == 'a triangle':
        triangle()
    elif ask == 'a rectangle':
        rectangle()
    elif ask == 'a pentagon':
        pentagon()
    elif ask == 'a hexagon':
        hexagon()
    elif ask == 'a heptagon':
        heptagon()
    elif ask == 'an octagon':
        octagon()
    elif ask == 'a nonagon':
        nonagon()
    elif ask == 'a decagon':
        decagon()
    elif ask == 'a hendecagon':
        hendecagon()
    elif ask == 'a dodecagon':
        dodecagon()