'''
Simple program to explain scope and functions
1. Global 
2. Local 
3. Built-in
'''

person_name = 'N/A'


def create_person(): 
	global person_name
	name = input('Enter a name: ')
	person_name = name

create_person()
print('Hello ' + person_name)