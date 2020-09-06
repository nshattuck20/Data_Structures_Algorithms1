'''
* The 'class' keyword creates a user defined objects 
that contains various attributes which determine it's behavior. 
'''


class Time: 
	'''
	Class that represents a time of the day. 
	'''
	def _init_(self): # constructor. 'Self' refers to this class
		self.hours = 0
		self.minutes = 0


'''Access the attributes of the class using the '.' dot operators (aka attribute reference 
operator)
'''

my_time = Time() 
my_time.hours = 7 
my_time.minutes = 15 

print('%d hours' % my_time.hours, end=' ')
print('and %d minutes' % my_time.minutes)