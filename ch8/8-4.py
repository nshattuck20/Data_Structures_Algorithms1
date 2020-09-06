'''
List slicing 

List slicing creates a new list and allows a programmer to 
store specified contents of a list within the new list object 
'''

players=['Rapinoe', 'Hamm', 'Lavelle', 'Horan']

print(players[0:3]) #Print from index 0-2
#Also can use negative indices 
print(players[0:-1]) # Contains all but the last index of the list 


nums = [1, 1, 2, 3, 5, 8, 13]
print(nums[5:10])


#stride example 

print(nums[0:4:2])