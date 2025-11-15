import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck in increasing order
        deck.sort()
        
        # Initialize a deque with positions 0 to n-1
        positions = deque(range(len(deck)))
        
        # Initialize the result list with None values
        result = [None] * len(deck)
        
        # Place each card in the sorted deck into the correct position
        for card in deck:
            result[positions.popleft()] = card
            if positions:
                positions.append(positions.popleft())
        
        return result

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    return Solution().deckRevealedIncreasing(deck)