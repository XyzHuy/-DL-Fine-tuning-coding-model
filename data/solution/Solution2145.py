import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Start with the initial prefix sum and the range of the first element
        prefix_sum = 0
        min_prefix = 0
        max_prefix = 0
        
        # Calculate the prefix sums and track the min and max values
        for diff in differences:
            prefix_sum += diff
            min_prefix = min(min_prefix, prefix_sum)
            max_prefix = max(max_prefix, prefix_sum)
        
        # Calculate the range of the first element that keeps the sequence within bounds
        # The first element can be in the range [lower, upper]
        # But we need to adjust it based on the range of prefix sums
        # The actual range for the first element is [lower - min_prefix, upper - max_prefix]
        min_start = lower - min_prefix
        max_start = upper - max_prefix
        
        # The number of valid starting points is the difference between max_start and min_start + 1
        # If min_start is greater than max_start, there are no valid sequences
        return max(0, max_start - min_start + 1)

def numberOfArrays(differences: List[int], lower: int, upper: int) -> int:
    return Solution().numberOfArrays(differences, lower, upper)