'''
10.7 A simple look at the Fibonacci Algorithm using Recursion
'''

def fibonacci(n):
    if (n == 0) or (n==1):
        return n
    else:
        '''
        Return fibonacci number up to n
        '''
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))