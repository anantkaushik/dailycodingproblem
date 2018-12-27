"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that 
all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
def sortColors(arr):
    if arr is None: return
    index, low, high = 0, 0, len(arr) - 1
    while(low <= high):
        if arr[low] == 'G':
            low += 1
        elif arr[low] == 'R':
            arr[index], arr[low] = arr[low], arr[index]
            index += 1
            low += 1
        elif arr[low] == 'B':
            arr[high], arr[low] = arr[low], arr[high]
            high -= 1
    return arr