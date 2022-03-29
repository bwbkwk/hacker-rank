# prepare fibonaci of 0, 1
table = {0:0,1:1,2:1}

def fibonacci(n):
    # if already calculated, just return the result
    if n in table:
        return table[n]
    # else calculate the fibonacci by its recursive definition
    # and save it in a table for the in other function.
    table[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return table[n]
    # Write your code here.
    
n = int(input())
print(fibonacci(n))
