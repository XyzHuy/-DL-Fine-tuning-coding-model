import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Count the occurrences of each number in the list
        num_counts = Counter(nums)
        
        # Sum the numbers that appear exactly once
        unique_sum = sum(num for num, count in num_counts.items() if count == 1)
        
        return unique_sum

def sumOfUnique(nums: List[int]) -> int:
    return Solution().sumOfUnique(nums)