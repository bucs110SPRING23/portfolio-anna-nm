class Rectangle: 
    def __init__(self, x, y, h, w):
        '''
        self.x: top left x-coordinate
        self.y: top left y-coordinate
        self.height: height of the rectangle
        self.width: width of the rectangle
        '''
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self): 
        '''
        return the value of the instance variables
        '''
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", height: " + str(self.height) + " ,width: " + str(self.width)


