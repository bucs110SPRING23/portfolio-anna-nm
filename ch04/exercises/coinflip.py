import turtle 
import random

window = turtle.Screen()
print(window.screensize()[0])

tt = turtle.Turtle()
tt.shape("turtle")

while True: 
    if tt.pos()[0] > window.screensize()[0] or tt.pos()[1] > window.screensize()[1]:        
        break
    n = random.randrange(1,3)
    if n == 1: 
        tt.right(90)
        tt.forward(50)
    else: 
        tt.left(90)
        tt.forward(50)
