import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(cap: int) -> bool:
            count = 0
            can_rob = True
            for num in nums:
                if can_rob and num <= cap:
                    count += 1
                    if count >= k:
                        return True
                    can_rob = False
                else:
                    can_rob = True
            return False
        
        low, high = min(nums), max(nums)
        while low <= high:
            mid = (low + high) // 2
            if can_rob_with_capability(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

def minCapability(nums: List[int], k: int) -> int:
    return Solution().minCapability(nums, k)