import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # Sort the weights to try and fit the lightest apples first
        weight.sort()
        
        total_weight = 0
        count = 0
        
        # Iterate over the sorted weights and add to the basket if possible
        for w in weight:
            if total_weight + w <= 5000:
                total_weight += w
                count += 1
            else:
                break
        
        return count

def maxNumberOfApples(weight: List[int]) -> int:
    return Solution().maxNumberOfApples(weight)