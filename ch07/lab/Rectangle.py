class Rectangle: 
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self): 
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", height: " + str(self.height) + " ,width: " + str(self.width)

print(Rectangle(2,1,4,5))
r = Rectangle(10, 10, 10, 10)
assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = Rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,1))
r = Rectangle(1, -5, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,5,1,1))
r = Rectangle(1, 1, -10, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,10,1))
r = Rectangle(1, 1, 1, -1000)
assert((r.x, r.y, r.height, r.width) == (1,1,1,1000))

    