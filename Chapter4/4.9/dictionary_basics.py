'''
Simple program demonstrating the basics of Dictionaries. 
'''

players = {'Lionel Messi' : 10, 
		   'Cristiano Ronaldo' : 7
		   }
print(players)

#Accessing an entry uses brackets [] with the specified key 
print('The value of this player is :' + str(players['Cristiano Ronaldo']))

#Editing the value of an entry 
players['Lionel Messi'] = 11
print(players)	

#Adding an entry 
players['Cristian Pulisic'] = 22
print(players)	   	

#Deleting an entry 
del players['Lionel Messi']
print(players)