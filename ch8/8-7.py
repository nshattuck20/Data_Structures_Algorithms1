'''
8-7 Dictionaries

* Key : value containers
* Unordered
'''

#Declaring a dictionary using {} brackets 
my_dict = {'Andrew'  : 'A+', 'Ryan' : 'B'}

#Declaring a dictionary using the dict() method 
my_new_dict =dict(Andrew= 'A+', Ryan = 'B+')

print(my_dict)
print()
print(my_new_dict)

'''
Common operations 
1. Indexing - retreives value of the key 
2. Adding entries if it does not exist, else modify 
3. Deleting entries 
4. Tests if a key exists 
'''

#Indexing a dictionary 

grade_andrew = my_dict['Andrew'] # get the value of the key 'Andrew'
print('Andrew :',grade_andrew)
grade_ryan = my_dict['Ryan']
print('Ryan:' ,grade_ryan)

#Adding an entry if it does not exist, else modify 
my_dict['Andrew'] = 'C'
my_dict['Austin'] = 'B+'

print('Andrew:', my_dict['Andrew'])
print('Austin:', my_dict['Austin'])

#Deleting an entry 
del my_dict['Ryan'] # deletes the key entry 'Ryan'
print('Deleting...')
print(my_dict)

#Testing if entry is in dictionary 
if 'Austin' in my_dict: 
	print('Found it!')

else:
	print('Keep looking')

#Dictionaries can hold arbitray values, including other containers 
my_dict['Austin'] = ['C+', 'A-', 'B', 'A'] # Dictionary with key 'Austin', whose values contain a list of grades
print(my_dict['Austin'])