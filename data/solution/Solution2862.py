import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        
        # Iterate over each starting index i
        for i in range(1, n + 1):
            current_sum = 0
            # Check all multiples of i where the product of indices is a perfect square
            j = 1
            while True:
                index = i * (j * j)
                if index > n:
                    break
                current_sum += nums[index - 1]
                j += 1
            max_sum = max(max_sum, current_sum)
        
        return max_sum

def maximumSum(nums: List[int]) -> int:
    return Solution().maximumSum(nums)