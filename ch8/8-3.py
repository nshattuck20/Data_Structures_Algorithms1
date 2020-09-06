'''
List nesting, or embedding a list inside of a list 
'''

my_list = [[10,20], [30,40]]
print('First nested list: ', my_list[0])
print('Second nested list:', my_list[1])
print('Element 0 of first list: ', my_list[0][0])


#Representing a tic-tac-toe board using nested lists 
tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])

scores = [
    [75, 100, 82, 76],
    [85, 98, 89, 99],
    [75, 82, 85, 5]
]
print('scores has', len(scores), 'elements that are lists')


#Iterating over multi-dimensional lists 
currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency: 
	for cell in row:
		print(cell, end='')
	print()

#Iterating ovefr a multi-dimensional list with enumerate()
for row_index, row in enumerate(currency):
	for column_index, item in enumerate(row):
		print('currency[%d][%d] is %.2f' % (row_index, column_index, item))