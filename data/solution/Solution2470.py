import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List
from functools import reduce

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_lcm = nums[i]
            for j in range(i, n):
                current_lcm = lcm(current_lcm, nums[j])
                if current_lcm == k:
                    count += 1
                elif current_lcm > k:
                    break
        
        return count

def subarrayLCM(nums: List[int], k: int) -> int:
    return Solution().subarrayLCM(nums, k)