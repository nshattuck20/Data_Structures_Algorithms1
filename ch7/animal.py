'''Simple program playing around with classes, and method objects'''

class Animal: 
	def __init__(self): 
		self.name = 'N/A'
		self.noise ='N/A'

	def make_noise(self, name, noise):
		print('I am a ' + self.name + ' and I go ' + self.noise)


cat = Animal() 
cat.noise = 'meow'
cat.name = 'cat'
cat.make_noise(cat.noise, cat.name)