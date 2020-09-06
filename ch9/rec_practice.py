'''
Some simple code to practice recursion basics 
Covers section(s) 9-2 -> 9.3
'''

def count_down(count, indent): 
	'''
	Recursively count down to zero
	'''
	if count == 0: 
		print(indent, 'Go!')
	else: 
		print(indent, count)
		count_down(count - 1, indent + '   ')

count_down(5, '   ')


