'''Print the 2-dimensional list mult_table by row and column. Hint: Use nested loops. Sample output for the given program:
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9
'''

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]


s = ""

for row in mult_table: 
	for cell in row: 
		if s!="":
			s+=" | "
		s+= str(cell) + " "
print(s)

