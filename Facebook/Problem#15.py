"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random
def pick(nums):
    randomElement = None
    for i,data in enumerate(nums):
        if i == 0:
            randomElement = data
        elif random.randint(1,i+1) == 1:
            randomElement = data
    return randomElement