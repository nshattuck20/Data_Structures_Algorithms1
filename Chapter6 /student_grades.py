'''
Simple program to create, update, and delete student grades 
in a classroom 
'''

def add_grade(student_grades): 
	grade_prompt = "Enter name and grade (Ex. 'Bob A+'): \n"
	name, grade = input(grade_prompt).split()
	print('Adding grade. \n')
	student_grades[name] = grade
	

def delete_grades(student_grades):
	print('Removing grade')
	name = input(delete_prompt)
	del student_grades[name]

def print_grades(student_grades):
	print("Printing grades \n")
	for name, grade in student_grades.items(): 
		print(name, 'has a ', grade)

student_grades = {} #Empty student dictionary 

menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

delete_prompt = "Enter name to delete:"

command = input(str(menu_prompt))


while command != '4': #Exit when user hits 4 
    if command == '1':
    	add_grade(student_grades)
    elif command == '2': 
    	delete_grades(student_grades)
    elif command == '3': 
    	print(student_grades)
    else: 
    	print('Unrecognized input \n')
