import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert the jewels string into a set for O(1) average time complexity lookups
        jewels_set = set(jewels)
        
        # Initialize a counter for the number of jewels found in stones
        count = 0
        
        # Iterate over each stone in the stones string
        for stone in stones:
            # If the stone is in the jewels set, increment the counter
            if stone in jewels_set:
                count += 1
        
        # Return the total count of jewels found in stones
        return count

def numJewelsInStones(jewels: str, stones: str) -> int:
    return Solution().numJewelsInStones(jewels, stones)