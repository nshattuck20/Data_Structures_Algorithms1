'''7.3 Class methods'''

class Time: 
	def __init__(self):
		self.hours = 0
		self.minutes = 0

	def print_time(self):
		print('hours: ', self.hours , end=' ')
		print('minutes: ', self.minutes)

time1 = Time()
time1.hours = 7 
time1.mimnutes = 15 
time1.print_time()

