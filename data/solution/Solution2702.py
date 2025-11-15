import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def canMakeNonPositive(k):
            # Calculate the total decrement needed if we perform k operations
            total_decrement_needed = 0
            for num in nums:
                # If num can be made non-positive in k operations by choosing it
                if num > k * y:
                    # We need to choose this index (num - k*y) / (x - y) times
                    total_decrement_needed += math.ceil((num - k * y) / (x - y))
            # If the total operations needed is less than or equal to k, it's possible
            return total_decrement_needed <= k
        
        # Binary search to find the minimum number of operations
        left, right = 0, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canMakeNonPositive(mid):
                right = mid
            else:
                left = mid + 1
        return left

def minOperations(nums: List[int], x: int, y: int) -> int:
    return Solution().minOperations(nums, x, y)