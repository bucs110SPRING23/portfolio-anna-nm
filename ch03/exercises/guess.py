import random

x = random.randrange(1,10)
for i in range(3): 
    k = int(input("Select a number: "))
    if k == x: 
        print("correct")
        break
    elif k < x: 
        print("Too low")
    else: 
        print("Too high")