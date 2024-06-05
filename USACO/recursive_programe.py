#Recursive program for the Fibonacci sequence

def f(n):
    #needs to have a condition to end
    if n == 1 or n == 2:
        return 1
    
    #needs to containt itslef
    else:
        return f(n-1) + f(n-2)

print(f(int(input('Enter a number : '))))