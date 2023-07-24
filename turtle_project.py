# this turtle project is unique circle

from  turtle import *
t=Turtle()
win=Screen()
win.title("Susanta")   # this is windows name
win.bgcolor("purple")    # window color
t.pensize(10)            #pen size
for i in range(6):   #total circle run 6 time
    t.color("Lime")  #circle color
    t.circle(120,95)   #round of circle
    t.color("yellow")   #circle color
    t.circle(120,85)
    t.circle(60,95)
    t.color("Lime")
    t.circle(60,170)
    t.color("yellow")
    t.circle(60,95)
    t.circle(120,85)
    t.color("Lime")
    t.circle(120,95)
    t.left(60)
# t.hideturtle()
done()


