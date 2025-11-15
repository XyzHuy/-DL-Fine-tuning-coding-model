import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        min_num = min(nums)
        max_num = max(nums)
        
        count = 0
        for num in nums:
            if min_num < num < max_num:
                count += 1
        
        return count

def countElements(nums: List[int]) -> int:
    return Solution().countElements(nums)