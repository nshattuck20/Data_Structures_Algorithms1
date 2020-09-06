'''
From Section 10.6: Recursive cumulativeSum algorithm
'''

def CumulativeSum(N):
    if N == 0:
        return 0 # Base Case
    else:
        return N + CumulativeSum(N-1) #Recursive Case

print(CumulativeSum(5)) # Return 15, or 5 + 4 + 3 + 2 + 1
