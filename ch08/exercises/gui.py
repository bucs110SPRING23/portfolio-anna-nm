class Block(): 
    def __init__(self, left=0, right=0, top =0, bottom=0, x=0, y=0): 
        self.mystery = True
        self.pos = (x,y)
        self.size = (left, right, top, bottom)
class Text(): 
    def __init__(self, font = None, pos = None) -> None:
        self.color = "white"
        self.size = 5
        self.font = None
        self.pos = None
class Coins():
        def __init__(self, nums=0, size=5) -> None:
            self.nums = nums
            self.color = "yellow"
            self.size = size