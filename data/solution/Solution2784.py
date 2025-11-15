import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        # Check if the length of nums is n + 1
        if len(nums) != n + 1:
            return False
        
        # Create the base array
        base = list(range(1, n)) + [n, n]
        
        # Count the frequency of elements in nums
        num_counts = Counter(nums)
        
        # Count the frequency of elements in base
        base_counts = Counter(base)
        
        # Compare the two frequency counts
        return num_counts == base_counts

def isGood(nums: List[int]) -> bool:
    return Solution().isGood(nums)