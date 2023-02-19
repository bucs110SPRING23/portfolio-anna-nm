import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#Race 1
michelangelo.pendown()
leonardo.pendown()
t1 = random.randrange(1,101)
t2 = random.randrange(1,101)
michelangelo.forward(t1)
leonardo.forward(t2)

michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Race 2
michelangelo.pendown()
leonardo.pendown()

for i in range(10):
    d1 = random.randrange(1,11)
    d2 = random.randrange(1,11)
    michelangelo.forward(d1)
    leonardo.forward(d2) 

michelangelo.penup()
leonardo.penup()
michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)

window.exitonclick()

#PART B
pygame.init()
window = pygame.display.set_mode()
window.fill("white")


num_sides = [3,4,6,20,100,360]
side_length = 100
for sides in num_sides:
    points = []
    angle = 360/sides
    xpos = 100
    ypos = 100
    radians = math.radians(angle * i)
    for i in range(sides):
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        
        print(x,y)
        points.append((x,y))
    pygame.draw.polygon(window, "brown",points)
    pygame.display.flip()
    pygame.time.wait(2000)