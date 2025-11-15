import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_set = set(nums)
        count = 0
        
        # Check each possible GCD from 1 to max_num
        for g in range(1, max_num + 1):
            current_gcd = None
            for multiple in range(g, max_num + 1, g):
                if multiple in nums_set:
                    if current_gcd is None:
                        current_gcd = multiple
                    else:
                        current_gcd = gcd(current_gcd, multiple)
                    # If at any point the current_gcd becomes g, we found a valid GCD
                    if current_gcd == g:
                        count += 1
                        break
        
        return count

def countDifferentSubsequenceGCDs(nums: List[int]) -> int:
    return Solution().countDifferentSubsequenceGCDs(nums)