def multiply(a, b): 
    ans = 0
    for i in range(a): 
        ans += b
    return ans

def exponent(base, exp): 
    ans = 1
    for i in range(exp): 
        ans = multiply(ans, base)
    return ans

def square(n):  
    return exponent(n, 2)

#test
print(multiply(2, 3),
    exponent(2,3),
square(2))
