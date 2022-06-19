## non-recursive version

def bigFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

## recursive version

def bigFactorialR(n):
    if n == 1:
        return 1
    else:
        return n * bigFactorial(n-1)
    
## test
print(bigFactorial(25))