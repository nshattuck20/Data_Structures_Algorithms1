'''
This is a simple program to practice:
1. Selection sort
2. Linear Search
3. Binary Search
'''

def selection_sort(numbers):
    for i in range(len(numbers)):
        #Find index of the smallest element
        index_smallest = i
        for j in range(i  + 1, len(numbers)):

            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        #Swap numbers[i] and numbers[indexSmallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


def linear_search(key, numbers):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i # return the index of key
    return -1 # key not found

def binary_search(key, numbers):
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
    while high>=low:
        mid = (high + low)//2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1 # not found

def recursive_binary_search(low, high, numbers, key):
    if low > high:
        return -1
    mid = (low + high)//2
    if numbers[mid]< key:
        return recursive_binary_search(mid+1, high, numbers, key)
    elif numbers[mid] > key:
        return recursive_binary_search(low, mid -1, numbers, key)
    else:
        return mid



#Some test code to show that the swap works
numbers = [9,2,11,1,3,6]
print('UNSORTED:', numbers)
selection_sort(numbers)
print('SORTED:', numbers)

#testing linear search
key_index = linear_search(2, numbers)
print('Linear Search: ', key_index)

#testing binary search
key_index = binary_search(11, sorted(numbers))
print('Binary Search:', key_index)

#testing recursive binary search
key_index = recursive_binary_search(0, len(numbers) -1, sorted(numbers), 3)
print('Recursive Binary Search: ', key_index)