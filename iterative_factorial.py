# Recursive factorial implementation
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

# Iterative solution
def factorial_iter(n):
    result = 1

    for i in range(1, n+1):
        result = result * i
    
    return result
    
assert factorial_iter(23) == 25852016738884976640000