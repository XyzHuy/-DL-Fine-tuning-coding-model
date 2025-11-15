import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Count the frequency of each number in nums
        num_counts = Counter(nums)
        # Get the unique numbers and sort them in ascending order
        unique_nums = sorted(num_counts.keys())
        operations = 0
        
        # Iterate over the sorted unique numbers except the smallest one
        for i in range(1, len(unique_nums)):
            # The number of operations needed to reduce all occurrences of the current number
            # is the number of operations needed for the previous number plus the count of the current number
            operations += num_counts[unique_nums[i]] * i
        
        return operations

def reductionOperations(nums: List[int]) -> int:
    return Solution().reductionOperations(nums)