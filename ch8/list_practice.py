'''
This is a practice project I came up with to 
practice lists, looping lists to modify/delete values, 
and list comprehensions. 

The solutions are in section 8.6 
'''

###Complete using loops only#####
#1. Write  a loop modifying a list by  adding 10 to every element. 

# my_list = [10,20,30]
# for i in range(len(my_list[:])):
# 	my_list[i] += 10 
# print('New list:', my_list)

#2. Write a program that gets input from a user into a list, then 
#converts each value of the list to a string. 

# user_input = input('Enter some numbers: ')
# values = user_input.split()
# strings = []
# for val in range(len(values)):
# 	str(strings.append(values[val]))

# print('List of strings :', strings)


#3. Write a program that gets input from a user into a list, then 
#converts each value of the list to an integer. 

# user_input = input('Enter some numbers: ')
# values = user_input.split()
# integers = []
# for val in range(len(values)):
# 	integers.append(int(values[val]))

# print('List has been converted to integers :', integers)
# print(type(integers))

#4. Find the sum of each row in a 2-D list.

# my_list = [
# [10, 20, 30], 
# [40,50,60]
# ]

# for row in range(len(my_list)): 
# 	print(sum(my_list[row]))


#5. Find the sum of the row with the smallest sum in a 2-D list. 

# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# sum_list = []
# for row in my_list:
#     sum_list.append(sum(row))
# min_row = min(sum_list)
# print(min_row)

#####Complete with list-comprehensions#######

#1. Write  a loop modifying a list by  adding 10 to every element. 

# my_list = [10,20,30,40,50]
# my_list = [(i + 10) for i in my_list]
# print(my_list)

#2. Write a program that gets input from a user into a list, then 
#converts each value of the list to a string. 

# user_input = input('Gimme numbers: ')
# tokens = user_input.split()
# my_list = []
# my_list = [str(token)for token in tokens]
# print(my_list)

#3. Write a program that gets input from a user into a list, then 
#converts each value of the list to an integer. 

# user_input = input('Gimme numbers: ')
# tokens = user_input.split()
# my_list = []
# my_list = [int(token)for token in tokens]
# print(my_list)

#4. Find the sum of each row in a 2-D list.

my_list = [
    [10, 20, 30],
    [40, 50, 60]]
my_list = [(sum(row))for row in my_list]
print(my_list)

#5. Find the sum of the row with the smallest sum in a 2-D list. 

my_list = [
    [10, 20, 30],
    [40, 50, 60]]
my_list = [(sum(row)) for row in my_list]