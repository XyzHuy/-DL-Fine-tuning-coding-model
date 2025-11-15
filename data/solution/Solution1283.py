import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid_divisor(divisor):
            total = sum(math.ceil(num / divisor) for num in nums)
            return total <= threshold
        
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if is_valid_divisor(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

def smallestDivisor(nums: List[int], threshold: int) -> int:
    return Solution().smallestDivisor(nums, threshold)