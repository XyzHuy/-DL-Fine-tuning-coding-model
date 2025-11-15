import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        current_streak = 0
        
        for num in nums:
            if num == 0:
                current_streak += 1
                count += current_streak
            else:
                current_streak = 0
        
        return count

def zeroFilledSubarray(nums: List[int]) -> int:
    return Solution().zeroFilledSubarray(nums)