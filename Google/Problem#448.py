"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values 
of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should 
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
# Time Complexity: O(N)
# Space Comlexity: O(1)
def sortColors(colors):
    index, low, high = 0, 0, len(colors) - 1
    while low <= high:
        if colors[low] == 'G':
            low += 1
        elif colors[low] == 'R':
            colors[index], colors[low] = colors[low], colors[index]
            index += 1
            low += 1
        else:
            colors[high], colors[low] = colors[low], colors[high]
            high -= 1