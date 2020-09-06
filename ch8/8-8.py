'''
Dictionary methods 
1. clear()
2. get()
3. update()
4. pop()
'''


my_dict = {'Bob' : '1', 'Jane' : '2', 'John' : '3', 'Luna' : '4'}

# get() 
print(my_dict.get('Jane', 'N/A')) # returns the key if in dictionary otherwise default value 
print(my_dict.get('Austin', 'N/A'))

# pop() 
print(my_dict.pop('Luna')) # removes and returns the key value of the popped item 
print(my_dict)

# update() 

my_dict.update({'John':'99'})
print(my_dict)

# clear() 
my_dict.clear() 
print(my_dict)