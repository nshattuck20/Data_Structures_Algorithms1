'''
Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about the student_grades dictionary. 
Find the following:

1. Print the name and grade percentage of the student with the highest total of points
2. Find the average score of each assignment.
3. Find and apply a curve to each student's total score, such that the best student has 
100% of the total points.


'''


# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Colin': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Mary': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

#1.Print name & grade of student with highest total of points 
student_with_highest_grade = max(student_grades.keys())
names = student_grades.keys()
list_grades = list(student_grades.values())
highest_grade_list = max(list_grades)
print('Student with highest score: ', student_with_highest_grade)
print('Total points: ', sum(highest_grade_list) / 500)



#2.Find the average score of each assignment 
avg_scores = {}
assignments = ('A1', 'A2', 'A3', 'A4', 'A5')
scores = [0] * 5
for name in student_grades.keys():
    lst = student_grades[name] 
    for value in range(5):
        scores[value] += 0.2 * lst[value]

for value in range(len(assignments)):
	avg_scores[assignments[value]] = scores[value]

for ass, scr in sorted(avg_scores.items()):
    print('{}, {: .2f}'.format(ass,scr)) 


	  

	  






	

		


	





