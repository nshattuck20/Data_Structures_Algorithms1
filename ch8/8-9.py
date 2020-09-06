'''
8-9 Iterating over a dictionary : 

3 methods 
1. dict.items() - returns view object yielding key/value tuples
2. dict.keys() - returns view object of dictionary keys
3. dict.values() - returns view object of dictionary values 
'''

##EXAMPLES OF METHODS###

# dict.items()
print("Example of using dict.items()")
pokemon_type = dict(Pikachu = 'Electric', Squirtle = 'Water', Charmander='Fire')
for name, type in pokemon_type.items():  # return a key/value tuple
	print('%s: %s' % (name, type))
print()
print("Example of using dict.keys()")
# dict.keys()
for name in pokemon_type.keys(): 
	print('%s' % name)

print()
print("Example of using dict.values()")
#dict.values()
for type in pokemon_type.values(): 
	print('%s ' % type)

'''
Dictionaries do not support indexing. 
This is because instead creating a new list, iteration 
evaluates each index individually, saving memory. 
To index, conver the dictionary to a list using the list()
method, as shown here. 
'''

#converting a dictionary to a list using list() for indexing 
list_of_pokemon = list(pokemon_type)
first = sorted(list_of_pokemon)[0] # sort contents alphabetically 
print(first)