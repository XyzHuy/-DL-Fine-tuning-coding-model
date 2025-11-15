import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Generate all subarray sums
        subarray_sums = []
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Calculate the sum of the elements from index left to right (1-based index)
        result = sum(subarray_sums[left-1:right]) % (10**9 + 7)
        
        return result

def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    return Solution().rangeSum(nums, n, left, right)