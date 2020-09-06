'''
Section 9-1: 
Recursive Functions 
'''

#Example of recursive function
#I used the code from the animation example in the course material 

def count_down(count): 
    if count == 0: 
        print('Go!')
    else: 
        print(count)
        count_down(count -1)

count_down(2) # recursively call count_down 3 times. 



#Another example is a program that prints alphabet backward 

def backward_aplhabet(current_letter): 
    if current_letter == 'a':
        print(current_letter)
    else: 
        print(current_letter)
        prev_letter = chr(ord(current_letter) - 1)
        backward_aplhabet(prev_letter)

starting