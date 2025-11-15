import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        num_set = set(nums)
        
        for num in nums:
            if (num + diff) in num_set and (num + 2 * diff) in num_set:
                count += 1
                
        return count

def arithmeticTriplets(nums: List[int], diff: int) -> int:
    return Solution().arithmeticTriplets(nums, diff)