import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # Count the frequency of each element in nums
        num_counts = Counter(nums)
        
        # Check if any element appears more than twice
        for count in num_counts.values():
            if count > 2:
                return False
        
        return True

def isPossibleToSplit(nums: List[int]) -> bool:
    return Solution().isPossibleToSplit(nums)