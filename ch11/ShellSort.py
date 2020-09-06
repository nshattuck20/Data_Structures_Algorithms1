'''
Chapter 11.10
Demonstrates the Shell Sort/ Interleaved List Algorithm
'''

def insertion_sort_interleaved(numbers, start_index, gap):
    swaps = 0
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and numbers[j] < numbers[j - gap]:
            swaps+=1
            temp = numbers[j]
            numbers[j] = numbers[j-gap]
            numbers[j - gap] = temp
            j-= gap
    return swaps


def shell_sort(numbers, gap_values):
    swaps = []
    '''
    Calls the insertion_sort_interleaved function with various gap sizes.
    The algorithm has been modified to return the total number of swap operations required.
    '''
    for gap_value in gap_values:
        for i in range(gap_value):
            swaps.append(insertion_sort_interleaved(numbers, i, gap_value))
        return swaps

numbers = [99, 2, 45, 1, 22, 9, 32, 6]
print('UNSORTED', numbers)
swaps = shell_sort(numbers, [1, 3, 7])
print('SORTED', numbers)
print('NUMBER OF SWAPS:', swaps)