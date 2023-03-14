import turtle 

side = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))

window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.color("brown")

for i in range(side):
    my_turtle.forward(length)
    my_turtle.left(360/side)

window.exitonclick()

