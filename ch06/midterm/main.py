import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
def drawRotate90(length): 
    pen.forward(length)
    pen.left(90)

def wall(pos = (-200,-200)):
    pen.color('papayawhip')
    pen.begin_fill()
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    drawRotate90(400)
    drawRotate90(300)
    drawRotate90(400)
    drawRotate90(300)
    pen.end_fill()
    
def roof(pos = (-200, 100)):
    pen.color('salmon')
    pen.begin_fill()
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    pen.forward(400)
    pen.goto(0, 300)
    pen.goto(-200, 100)
    pen.end_fill()
    
def door(pos = (-50, -200), color = 'rosybrown'): 
    pen.color(color)
    pen.begin_fill()
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    drawRotate90(100)
    drawRotate90(150)
    drawRotate90(100)
    drawRotate90(150)
    pen.end_fill()
    
def doorknop(pos = (-30, -120), color = 'saddlebrown'):
    pen.color(color)
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    pen.dot(16)
    
def window(pos1 = (-160, 0), pos2 = (80, 0),  color = 'lightblue'):
    pen.color(color)
    pos_list = [pos1, pos2]
    for pos in pos_list:
        pen.begin_fill()
        pen.penup()
        pen.goto(pos)
        pen.pendown()
        for i in range(4):
            drawRotate90(80) 
        pen.end_fill()

def drawHouse():
    wall()
    roof()
    door()
    doorknop()
    window()

if __name__ == "__main__":
    drawHouse()
    screen.exitonclick()


