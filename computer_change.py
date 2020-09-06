'''
A cashier distributes change using the maximum number of five dollar bills, followed 
by one dollar bills. For example, 19 yields 3 fives and 4 ones. 
Write a single statement that assigns num_ones with the number of distributed 1 
dollar bills given amount_to_change. 
Hint: Use %.
'''

amount_to_change = 19
num_fives = amount_to_change // 5

num_ones = amount_to_change % 5

print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')