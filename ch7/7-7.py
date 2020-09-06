'''Class customization 
	* Referes to how classes can be altered by rhe 
		programmer to suit her needs. 
	* _str_() changes how to print the output of an object 
'''

class Toy: 
	def __init__(self, name, price, min_age): 
		self.name = name 
		self.price = price 
		self.min_age = min_age 

truck = Toy('Monster Truck X', 14.99, 5)
print(truck) # print the memory address of truck 


class Toy: 
	'''
	Using the __str__() special method name to change 
	the output of the Toy object. 
	'''
	def __init__(self, name, price, min_age): 
		self.name = name 
		self.price = price 
		self.min_age = min_age 

	def __str__(self): 
		return ('%s costs only $%.2f. Not for children under %d!' % 
                (self.name, self.price, self.min_age))
truck = Toy('Monster Truck X', 14.99, 5)
print(truck)

'''
Operator overloading using rich comparison methods: 
__lt__(self, other) less-than(<)
__gt__(self, other) greater-than(>)
__le__(self, other) less-than or equal-to(<=)
__ge__(self, other) greater-than or equal-to(>=)
__eq__(self, other) equal to (==)
__ne__(self, other) not-equal to (!=

)
'''