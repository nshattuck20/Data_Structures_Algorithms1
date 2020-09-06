
'''
Data Structures and Algorithms 1 
This unit goes into detail about: 
    -membership operators 
    -identity operators 
    -identity operators vs relational operators 
'''



'''
Membership operators 
-Two membership operators 
	#1. in
	#2. not in 
'''


####Uncomment below to run the code#####
'''
#Check if a certain value is within the list 
colors = ['Red', 'Green', 'Blue', 'Yellow']

if 'Red' in colors: 
	print('Found color')

if 'Orange' not in colors: 
	print('Sorry, I cannot find that shit man.')

'''

#####Uncomment below to run######
'''
#Check if a value is within a dictionary

players = {'Cristian Pulisic' : 11, 'Weston McKinnie' : 9, 'Zack Steffen' : 1}

player = input('Please enter a player and i will see if he is on the roster: ')

if player in players: 
	print(player + ' is on the roster.')
elif player not in players: 
	print(player + ' not on roster.')


'''


#Identity operators 
	# 1. is 
	# 2. is not 

x = 100 
y = 100
print(x is 100)
print(y is 20)
print(x is y)
print(x == y)