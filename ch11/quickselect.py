'''
Chapter 11.21
Quickselect algorithm:
Recursive algorithm to find the kth smallest index in a list
'''

def partition(numbers, start_index, end_index):
    '''
    Organizes elements between the start and end indices so that the left part elements are less than or equal
    to the pivot and the right part elements are greater than or equal to the pivot. The left and right portions
    may be different sizes, and the method returns the last item in the left part's index.
    The left and right parts are not, themselves, sorted.

    The partition method has an O(N) runtime complexity.
    '''

    #Select the middle point
    midpoint = start_index + (end_index - start_index)//2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other low ->  <- high
    low = start_index
    high = end_index

    done = False
    while not done:
        #Increment while numbers[low] < pivot
        while numbers[low] < pivot:
            low = low + 1

        #Decrement while pivot < numbers[high]
        while pivot < numbers[high]:
            high = high - 1
        # If low and high have crossed each other the loop is finished.
        # If not, then swap the elements. Low is incremented and high is
        # decremented.
        if low >= high:
            done = True
        else:
            temp = numbers[low]
            numbers[low] = numbers[high]
            numbers[high] = temp
            low = low + 1
            high = high - 1
    # high is the last index in the left segment
    return high

# Selects kth smallest element, where k is 0-based
def quickselect(numbers, first, last, k):
   if (first >= last):
      return numbers[first]

   lowLastIndex = partition(numbers, first, last)

   if (k <= lowLastIndex):
      return quickselect(numbers, first, lowLastIndex, k)
   return quickselect(numbers, lowLastIndex + 1, last, k)

list = [15,73,5,88,9]
print(quickselect(list, 0, len(list) - 1, 3))
