"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
write a function that shuffles a deck of cards represented as an array using only swaps.
It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import random
def shuffleCards(cards):
    for i in range(1,len(cards)):
        n = random.randint(0,i)
        cards[i], cards[n] = cards[n], cards[i]
    return cards