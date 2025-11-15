import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        count = 0
        length = 1
        
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                count += (length * (length + 1)) // 2
                length = 1
        
        # Add the last alternating sequence
        count += (length * (length + 1)) // 2
        
        return count

def countAlternatingSubarrays(nums: List[int]) -> int:
    return Solution().countAlternatingSubarrays(nums)