import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List

class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        def find_gcd_of_list(lst):
            x = lst[0]
            for i in lst[1:]:
                x = gcd(x, i)
                if x == 1:
                    return 1
            return x
        
        current_gcd = nums[0]
        splits = 1
        
        for num in nums:
            current_gcd = gcd(current_gcd, num)
            if current_gcd == 1:
                splits += 1
                current_gcd = num
        
        return splits

def minimumSplits(nums: List[int]) -> int:
    return Solution().minimumSplits(nums)