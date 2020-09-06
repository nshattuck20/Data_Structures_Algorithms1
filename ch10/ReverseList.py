'''
From 10.6: Recursive Functions
An explanation of the Reverse List Algorithm:
Given a list, swap the first and last elements of the list until finished
'''

def ReverseList(lst):
    if not lst:#Base case. This is if lst == []
        return lst
    return lst[-1:] + ReverseList(lst[:-1]) #Recursive Case 

#Demo
print(ReverseList([1,2,3,4,5])) #[5,4,3,2,1]