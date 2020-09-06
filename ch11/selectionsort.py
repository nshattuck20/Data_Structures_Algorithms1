'''
Chapter 11.5
Selection Sort example
A selection sort is an algorithm that has two components:
    1. sorted
    2. unsorted
'''


def selection_sort(numbers):
    for i in range(len(numbers) - 1):

        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):

            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


numbers = [9, 3, 5, 18, 12]
print('UNSORTED:', numbers)
selection_sort(numbers)
print('SORTED:', numbers)
