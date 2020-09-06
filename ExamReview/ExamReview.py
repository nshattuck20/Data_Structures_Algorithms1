# Syntax for getting a new list with elements of the 2nd list added to the first
my_list = [1,2,3]
my_list_second = [4,5]
combined_list = my_list + my_list_second
print(combined_list)

# Basic dictionary operations...
my_dict = {"Bob" : 1,
           "Sara": 2,
           "Nick": 4
        }

print(my_dict)

# Get returns the value of the specified key
print("Value of Sara:", my_dict.get("Sara"))

# Pop removes the first item in the dictionary
my_dict.pop("Bob")
print(my_dict)

# Update modifies a specified value of dictionary
my_dict.update({"Bob": 5})
print(my_dict)

# Clear removes all items from dictionary
my_dict.clear()
print(my_dict)
