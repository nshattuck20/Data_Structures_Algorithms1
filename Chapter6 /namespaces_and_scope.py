'''
Using globals() ans locals() to get namespaces
'''
print('Initial global namespace: ')
print(globals())


my_var = "This is a variable"
print('\nCreated new variable')
print(globals())

def my_func():
    pass

print('\nCreated new function')
print(globals())