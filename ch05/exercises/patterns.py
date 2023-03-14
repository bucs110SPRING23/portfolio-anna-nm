n = int(input("Enter the number of rows: "))
def star_pyramid(n):
  for i in range(n): 
    print("*" * (i+1))

def rstar_pyramid(n):
  for i in range(n, 0, -1): 
    print("*" * i)

#test
star_pyramid(n)
rstar_pyramid(n)

