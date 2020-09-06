'''
8-10: Nested dictionaries 
(Dictionaries within dictionaries)
'''
# To declare a nested dictionary, do the following:
students = {}  # empty dictionary
'''
#Create indexing operation with key 'John and value of another dictionary'
print('John:')

###EXAMPLE####
'''
# students['John'] = {'Grade' : 'A+' , 'StudentID' : 22321}
# print('Grade: %s' % students['John'] ['Grade']) # obtain the value of key 'John' from students. Yields nested dictionary.
# print('StudentID: % s' % students['John']['StudentID'])

music = {
    'Artists': {
        'Pink Floyd': {
            'Albums': {
                'The Dark Side of The Moon': {
                    'Songs': ['Speak To Me', 'Breathe', 'On the Run', 'Money'],
                    'Year': 1974,
                    'Platinum': True
                }
            }
        }
    }

}

user_input = input('Enter artist name: ')

while user_input != 'exit': 
	if user_input in music: 
		#Get the values from the dict
		artists = music[user_input]['Artists']
		albums = music[user_input]['Albums']
		songs = music[user_input]['Songs']

		#print values in the list 
		for val, songs in enumerate(songs): 
			print('Songs: %s %s ' % (val,songs))

	print('Albums: %s' %s albums)
	print('Artist: %s' %s artists)







#####Simple music program######
'''
The following program uses nested dictionaries to store a small music library. 
Extend the program such that a user can add artists, albums, and songs to the library.
'''

# 1. Add a command that adds an artist name to the music dictionary
# 2. Add commands for adding albums and songs
# 3. Take care to check that an artist exists in the dictionary before adding an album,
#    and that an album exists before adding a song

########################EXERCISE#############################



