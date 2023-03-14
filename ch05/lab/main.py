import pygame

#PART A:
def threenp1(n):
    n = float(n)
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

def threenp1range(upper_limit):
    threenp1_dict = {}
    for i in range(2, upper_limit+1): 
        threenp1_dict[i] = threenp1(i)
    return threenp1_dict

if __name__ == "__main__":
    print(threenp1range(5))

#PART B 
