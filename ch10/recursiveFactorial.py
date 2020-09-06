'''
From chapter 10.6: Recursive Functions
'''

def factorial(N):
    if N == 1: #Base Case
        return 1
    else:
        return N * factorial(N-1) #Recursive Case. 

print(factorial(6))
