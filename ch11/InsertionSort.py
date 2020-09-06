'''
Chapter 11.8 Insertion Sort

Insertion Sort is a sorting algorithm that sorts 2 parts:
    1. Sorted
    2. Unsorted

   *  Variable i is the first sorted element. It starts at i = 1 as it is assumed
    the first element is sorted.
    * Variable j keeps track of the index of the current element being sorted.
    If j is less than the element to the left ([j-1]), then the values are
    swapped.
'''

def insertion_sort(numbers):
    for i in range(len(numbers)):
        j = i
        # Insert num_list[i] into sorted part
        # stopping once num_list[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1 ]:
            # Swap num_list[j] and num_list[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp
            j-=1
    return numbers

numbers = [3,1,7,5,9]
print('UNSORTED', numbers)
insertion_sort(numbers)
print('SORTED', numbers)
