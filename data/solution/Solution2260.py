import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Dictionary to store the last seen index of each card value
        last_seen = {}
        min_length = float('inf')
        
        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the distance between the current and last seen index of the card
                min_length = min(min_length, i - last_seen[card] + 1)
            # Update the last seen index of the card
            last_seen[card] = i
        
        # If min_length is still infinity, it means no matching pair was found
        return min_length if min_length != float('inf') else -1

def minimumCardPickup(cards: List[int]) -> int:
    return Solution().minimumCardPickup(cards)