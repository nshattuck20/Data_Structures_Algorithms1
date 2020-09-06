'''
Adding parameters to a constructor
'''

class RaceTime: 
	distance = 0 

	def __init__(self,start_time, end_time, distance):
		self.start_time = start_time
		self.end_time = end_time
		self.distance = distance

	def print_time(self): 
		print("Start time -- "+ self.start_time + " End time -- " + self.end_time)

time_jason = RaceTime('3:15', '7:45', 26.21875)
time_nick = RaceTime('3:15', '6:30', 26.21875)
time_nick.print_time()
