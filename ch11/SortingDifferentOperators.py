'''
Chapter 11. 19
Uncomment the code blocks below to test.
'''

import operator
# Sorting a list using sorted()
# unsorted_list = [3,1,0,11,42, 4]
# sorted_list = sorted(unsorted_list)
# print("UNSORTED", unsorted_list)
# print("SORTED", sorted_list)
#
# # Sorting a list using sort()
# unsorted_fruit = ['apple', 'grape', 'bananna', 'orange', 'mango','lime']
# print("UNSORTED", unsorted_fruit)
# print("SORTED", unsorted_fruit.sort()) # returns None
# unsorted_fruit.sort()
# print(unsorted_fruit) # Sorts fruit in ascending order.
'''
sorted() and sort() can take optional keyword arguments, 'reverse', that when set to True, 
reverses the list in descending order. 
'''
# num_list = [3, 7, 2, 8, 12, 4, 9, 5]
# sorted_num_list = sorted(num_list, reverse = True)
# print('UNSORTED:', num_list)
# print('REVERSE SORTED:', sorted_num_list)
# print()
#
# fruit_list = ["grape", "banana", "apple", "strawberry", "blueberry"]
# print('UNSORTED:', fruit_list)
# fruit_list.sort(reverse = True)
# print('REVERSE SORTED:', fruit_list)

'''
Sorting with key function. 
You can also use sort() and sorted() with an optional key function. 
It can, for example, sort a list without regards to letter casing. 
sort() and sorted() will sort capital letters before lower case. 
'''

# # Program to sort strings using str.lower
# file_names = [ "Grades.xls", "email.txt", "helper.py", "Test.java" ]
# case_sensitive = sorted(file_names)
# case_insensitive = sorted(file_names, key = str.lower)
# print('Normal sort:', case_sensitive)
# print('Case insensitive sort:', case_insensitive)

# Example of using a custom key function
# def key_is_name(element):
#     return element[0]
#
#
# def key_is_id(element):
#     return element[1]
#
#
# class_list = [("Robert", 135216), ("Amir", 612901), ("Jennifer", 194821), ("Ravi", 631104)]
# name_result = sorted(class_list, key=key_is_name)
# id_result = sorted(class_list, key=key_is_id)
# print('Sort by name:', name_result)
# print('Sort by id:', id_result)
#
# # Using sorted() with itemgetter()
# name_result = sorted(class_list, key = operator.itemgetter(0))
# id_result = sorted(class_list, key = operator.itemgetter(1))
# print('Sort by name:', name_result)
# print('Sort by id:', id_result)

'''
Exercise 11.19.3

'''
#1
num_list = [(10,14), (18,12)]
result = sorted(num_list, key = operator.itemgetter(1))
print(result)

#3
word_list = ['two','four','six', 'eight']
result = sorted(word_list, key = operator.itemgetter(2))
print(result)