import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Iterate over all possible starting points of subarrays
        for i in range(n):
            distinct_values = set()
            # Iterate over all possible ending points of subarrays starting from i
            for j in range(i, n):
                distinct_values.add(nums[j])
                # Calculate the distinct count for the subarray nums[i..j]
                distinct_count = len(distinct_values)
                # Add the square of the distinct count to the total sum
                total_sum += distinct_count ** 2
        
        return total_sum

def sumCounts(nums: List[int]) -> int:
    return Solution().sumCounts(nums)