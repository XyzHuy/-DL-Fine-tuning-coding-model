import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # Dictionary to store the count of remainders when divided by 24
        remainder_count = defaultdict(int)
        complete_day_pairs = 0
        
        for hour in hours:
            # Calculate the remainder of the current hour when divided by 24
            remainder = hour % 24
            
            # Calculate the complement that would sum with the current remainder to form a complete day
            complement = (24 - remainder) % 24
            
            # Add the count of the complement in the dictionary to the pair count
            complete_day_pairs += remainder_count[complement]
            
            # Increment the count of the current remainder in the dictionary
            remainder_count[remainder] += 1
        
        return complete_day_pairs

def countCompleteDayPairs(hours: List[int]) -> int:
    return Solution().countCompleteDayPairs(hours)