'''
8-6 List Comprehensions: 

Form: 

new_list = [expression for name in iterable]

3 components: 
 1. The expression to evaluate each iterable component
 2. A loop variable to bind to the components
 3. An iterable object

'''

#Example 
my_list = [5, 10, 15]
my_list_plus5 = [(i + 5) for i in my_list]
print('New list contains' , my_list_plus5)