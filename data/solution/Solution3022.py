import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def canAchieve(target: int) -> bool:
            count = 0
            mask = ~target  # The bits we want to clear
            current = ~0
            for num in nums:
                current &= num
                if current & mask == 0:
                    # We can start a new group
                    current = ~0
                else:
                    count += 1
                    if count > k:
                        return False
            return True
        
        left, right = 0, (1 << 30) - 1
        while left < right:
            mid = (left + right) // 2
            if canAchieve(mid):
                right = mid
            else:
                left = mid + 1
        return left

def minOrAfterOperations(nums: List[int], k: int) -> int:
    return Solution().minOrAfterOperations(nums, k)