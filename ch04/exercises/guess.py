import random

x = random.randrange(1,1001)
count = 0
while True:
    k = int(input("Select a number: "))
    if k == x: 
        print("Correct number: ", k)
        count += 1
        print("Number of guesses: ", count)
        break
    elif k < x: 
        print("Too low")
        count += 1
    else: 
       print("Too high")
       count += 1