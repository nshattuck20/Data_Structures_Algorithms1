'''
This is a quick intro into the basic methods of lists:
pop()
remove()
append()
'''

my_list = [2000,2001,2002,2003,2004,2005]
print(my_list)

#append 2006 to my_list
my_list.append(2006)
print(my_list)

#pop the third  index (2003) from the list 
my_list.pop(3)
print(my_list)

#remove() removes the specidied value 
my_list.remove(2001)
print(my_list)

my_copy = [] 
print("Copied list before slice notation", my_copy)
for item in range(len(my_list)):
    # using slice notation
    my_copy = my_list[:]

print("Copied list after slice notation", my_copy)