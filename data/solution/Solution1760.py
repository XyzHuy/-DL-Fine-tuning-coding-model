import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(penalty):
            operations = 0
            for num in nums:
                if num > penalty:
                    operations += (num - 1) // penalty
            return operations <= maxOperations
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid
            else:
                left = mid + 1
        return left

def minimumSize(nums: List[int], maxOperations: int) -> int:
    return Solution().minimumSize(nums, maxOperations)