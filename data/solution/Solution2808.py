import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        # Dictionary to store the indices of each number
        index_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        min_seconds = n // 2  # Maximum possible time is half the length of the array
        
        for indices in index_map.values():
            # Calculate the maximum time needed to spread the current number
            max_time = 0
            for i in range(len(indices)):
                if i == 0:
                    # Calculate the time to spread from the last element to the first
                    max_time = max(max_time, (indices[i] - indices[-1] + n) // 2)
                # Calculate the time to spread between consecutive elements
                max_time = max(max_time, (indices[i] - indices[i - 1]) // 2)
            min_seconds = min(min_seconds, max_time)
        
        return min_seconds

def minimumSeconds(nums: List[int]) -> int:
    return Solution().minimumSeconds(nums)