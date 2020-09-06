'''
9-2: Recursive Algorithm: Search 

The following section demonstrates the recursive Binary Search 
algorithm. 
'''

def find(low, high): 
	mid = (low + high) // 2 # midpoint of low..high (// = floor division)
	answer = input('Is it %d? (l/h/y): ' % mid)

	if (answer != 'l') and (answer != 'h'): 
	    print('Got it!')
	else: 
	    if answer == 'l': 
	        find(low, mid)
	    else: 
	        find(mid + 1, high)

print('Choose a number from 0 to 100.')
print('Answer with:')
print('   l (your num is lower)')
print('   h (your num is higher)')
print(' any other key (guess is right).')

find(0, 100)

