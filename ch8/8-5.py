'''
8-5 Loops modifying lists
Uncomment below to try out the examples
'''

# '''
# The most basic way to modify a list is shown below.
# '''
# my_list = [3.2,5.0,16.5,12.25]
# print(my_list)
# for i in range(len(my_list)):
# 	'''Modify each value in the list by adding 5'''
# 	my_list[i] += 5

# print('Modified:', my_list)


# '''
# Now lets say we want to modify a list where
# if any negative number appears, we convert it to zero

# 1. The first way is the corrrect way
# 2. The second way is the incorrect way
# '''

# ########## THE CORRECT WAY ##########
# user_input = input('Enter numbers: ')

# tokens = user_input.split() # Convert each entry to into a string

# #convert each string into an integer
# nums = []
# for token in tokens:
# 	nums.append(int(token))

# #Print each number and position
# print()
# for pos, val in enumerate(nums):
# 	print('%d: %d' % (pos, val))

# #Change negative values to zero
# for pos in range(len(nums)):
# 	if nums[pos] < 0:
# 		nums[pos] = 0

# #Print new numbers
# print('New numbers: ')
# for num in nums:
# 	print(num, end='' )


# #### INCORRECT ####
# user_input = input('Enter numbers:')

# tokens = user_input.split()

# # Convert strings to integers
# nums = []
# for token in tokens:
#     nums.append(int(token))

# # Print each position and number
# print()
# for pos, val in enumerate(nums):
#     print('%d: %d' % (pos, val))

# # Change negative values to 0
# for num in nums:
#     if num < 0:
#         num = 0  # Logic error: temp variable num set to 0

# # Print new numbers
# print('New numbers: ')
# for num in nums:
#     print(num, end=' ')


# '''
# Modifying or changing the size of a list:

# 	* It's common practice to change the size of a list.
# 	* A common mistake is when attempting to modify/delete from a list
# 		and the program mistakenly shifts a value to an unintended position.
# 	*
# 	* The first program is the incorrect way of modification
# 	* The second program is the correct way.

#  '''

# numbers1 = []
# numbers2 = []

# u_input = input('Enter numbers for list 1: ')
# tokens = u_input.split()

#     # convert strings to integers
#    for pos, val in enumerate(tokens):
#         numbers1.append(int(val))
#         print('%d: %s' % (pos, val))

#     u_input = input('Enter numbers for list 2: ')
#     tokens = u_input.split()

#     for pos, val in enumerate(tokens):
#         numbers2.append(int(val))
#         print('%d: %s' % (pos, val))

#     # Remove elements from numbers1 if also in numbers2
#     for val in numbers1:
#         # INCORRECT #
#         if val in numbers2:
#             print('Deleting % d' % val)
#             numbers1.remove(val)
# # Print new numbers
# print('\nNumbers only in first set:', end=' ')
# for num in nums1:
#     print(num, end=' ')

#The correct way###
nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('%d: %s' % (pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))
    
# Remove elements from nums1 if also in nums2
print()
for val in nums1[:]:
	#Make a copy of nums1 list to correctly remove values
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')
