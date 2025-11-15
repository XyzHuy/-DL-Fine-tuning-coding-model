import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                # Decide whether to modify nums[i] or nums[i-1]
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                modified = True
        
        return True

def checkPossibility(nums: List[int]) -> bool:
    return Solution().checkPossibility(nums)