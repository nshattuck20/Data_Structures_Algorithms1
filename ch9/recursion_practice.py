'''
Practice problems 9-5 and 9-6

Problem 1. Given an integer input by the user, the function returns 
the Fibonacci sequence for the number of steps supplied by the user. 
For example, if user enters 8, return 0, 1, 1, 2, 3, 5, 8, 12
'''

def fibonacci(v1, v2, run_count):
    print(v1, '+', v2, '=', v1+v2)

    if run_count <= 1:  # Base Case
                                       # Run for users number of steps
        pass  # do nothing
    else:  # Recursive case
        fibonacci(v2, v1+v2, run_count-1)


print('This program outputs the\n'
      'Fibonacci sequence step-by-step\n'
      'starting after the first 0 and 1 \n')

run_for = int(input('How many numbers would you like?'))
fibonacci(0, 1, run_for)



