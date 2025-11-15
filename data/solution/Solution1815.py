import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache
from collections import Counter

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # Calculate the remainder of each group size when divided by batchSize
        remainders = [g % batchSize for g in groups]
        remainder_count = Counter(remainders)
        
        # Convert remainder_count to a tuple for memoization
        remainder_tuple = tuple(remainder_count[remainder] for remainder in range(batchSize))
        
        @lru_cache(None)
        def dp(remaining_donuts, remainder_tuple):
            # Convert the tuple back to a counter
            remainder_count = Counter({remainder: remainder_tuple[remainder] for remainder in range(batchSize)})
            
            # Base case: if no more groups to serve
            if sum(remainder_count.values()) == 0:
                return 0
            
            max_happy = 0
            for remainder in range(batchSize):
                if remainder_count[remainder] == 0:
                    continue
                
                # Serve a group with the current remainder
                new_remainder_count = remainder_count.copy()
                new_remainder_count[remainder] -= 1
                new_remaining_donuts = (remaining_donuts - remainder) % batchSize
                
                # Calculate the number of happy groups
                if remaining_donuts == 0:
                    happy_groups = 1 + dp(new_remaining_donuts, tuple(new_remainder_count[remainder] for remainder in range(batchSize)))
                else:
                    happy_groups = dp(new_remaining_donuts, tuple(new_remainder_count[remainder] for remainder in range(batchSize)))
                
                # Update the maximum number of happy groups
                max_happy = max(max_happy, happy_groups)
            
            return max_happy
        
        return dp(0, remainder_tuple)

def maxHappyGroups(batchSize: int, groups: List[int]) -> int:
    return Solution().maxHappyGroups(batchSize, groups)