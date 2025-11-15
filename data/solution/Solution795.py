import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = 0
            current_length = 0
            for num in nums:
                if num <= bound:
                    current_length += 1
                    ans += current_length
                else:
                    current_length = 0
            return ans
        
        return count(right) - count(left - 1)

def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
    return Solution().numSubarrayBoundedMax(nums, left, right)