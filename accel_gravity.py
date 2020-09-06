'''
Compute the acceleration of gravity for a given distance from the earth's center, 
dist_center, assigning the result to accel_gravity. 
The expression for the acceleration of gravity is: (G * M) / (d 2), 
where G is the gravitational constant 6.673 x 10-11, M is the mass of the 
earth 5.98 x 1024 (in kg) and d is the distance in meters from the earth's 
center (stored in variable dist_center).

Sample output for the given program:
9.803495445209855
'''

G = 6.673e-11
M = 5.98e24
dist_center = 6.38e6

accel_gravity = (G * M) / (dist_center**2)

print(accel_gravity)