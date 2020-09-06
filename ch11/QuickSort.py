'''
11.12 Python: Quick Sort
'''

#The partition() function of the quicksort() algorithm
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

def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements.
    if end_index <= start_index:
        return
    # Partition the list segment.
    # high is the end of the left segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    # high + 1 is the beginning of the right segment. 
    quicksort(numbers, high + 1, end_index)


# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers)-1)
print('SORTED:', numbers)