'''
Simple program that will convert hours into minutes. 
'''

hours = int(input('Enter hours:\n')) #1h = 60 min
minutes = int(input('Enter minutes: \n')) #1min = 0.0166666667 h
minutes_in_hour = hours * 60 + minutes

print(hours, 'hours is', end=' ')
print(minutes_in_hour, 'minutes', end='')