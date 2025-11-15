import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        MOD = 10**9 + 7
        diff_count = defaultdict(int)
        
        for num in nums:
            difference = num - rev(num)
            diff_count[difference] += 1
        
        nice_pairs = 0
        for count in diff_count.values():
            if count > 1:
                nice_pairs += (count * (count - 1) // 2) % MOD
        
        return nice_pairs % MOD

def countNicePairs(nums: List[int]) -> int:
    return Solution().countNicePairs(nums)