import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        
        for x in range(n + 1):
            if x == 0:
                if nums[0] < x:
                    return x
            elif x == n:
                if nums[-1] >= x:
                    return x
            else:
                if nums[x - 1] >= x and nums[x] < x:
                    return x
        
        return -1

def specialArray(nums: List[int]) -> int:
    return Solution().specialArray(nums)