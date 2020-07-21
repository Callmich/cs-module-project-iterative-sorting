def linear_search(arr, target):
    # Your code here
    for i in range (len(arr)):
        if arr[i] == target:
            return i
        else:
            i += 1
    return -1
    

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1


    firstIndex = 0
    lastIndex = len(arr) - 1

    

    while firstIndex < lastIndex:
        midpoint = int((lastIndex - firstIndex) / 2) 

        if target == arr[midpoint]:
            return midpoint
        elif target > arr[midpoint]:
            firstIndex = midpoint + 1
        else:
            lastIndex = midpoint - 1

    if arr[firstIndex] == target:
        return firstIndex
    return -1  # not found
