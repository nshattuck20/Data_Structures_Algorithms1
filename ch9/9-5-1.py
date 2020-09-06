'''
9-5-1
Write a program that outputs the nth Fibonacci number, where n is a 
user-entered number. So if the user enters 4, the program should 
output 3 (without outputting the intermediate steps). 
Use a recursive function compute_nth_fib that takes n as 
a parameter and returns the Fibonacci number. 
The function has two base cases: input 0 returns 0, and input 1 returns 1.
'''

def compute_nth_fib(num):
    # if base case ...
    if num == 0 or num == 1:
       return num
    else:
        return compute_nth_fib(num-1) + compute_nth_fib(num-2)
    #     return print(compute_nth_fib(num))
        
print('This program will find the nth Fibonacci \n'
      'number. Example: entering 4 returns 3, because\n'
      '3 is the 4th number in the Fibonacci sequence.\n')

nth_number = int(input('Which number would you like to find?'))
print(compute_nth_fib(nth_number))