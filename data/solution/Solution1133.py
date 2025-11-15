import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Count the occurrences of each number in the array
        count = Counter(nums)
        
        # Filter numbers that occur only once and find the maximum
        unique_numbers = [num for num, freq in count.items() if freq == 1]
        
        # Return the maximum unique number, or -1 if there are none
        return max(unique_numbers) if unique_numbers else -1

def largestUniqueNumber(nums: List[int]) -> int:
    return Solution().largestUniqueNumber(nums)