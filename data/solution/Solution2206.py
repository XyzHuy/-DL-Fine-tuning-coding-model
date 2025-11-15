import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Count the frequency of each number in the array
        num_counts = Counter(nums)
        
        # Check if every number appears an even number of times
        for count in num_counts.values():
            if count % 2 != 0:
                return False
        
        return True

def divideArray(nums: List[int]) -> bool:
    return Solution().divideArray(nums)