import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        end0, end1, end2 = 0, 0, 0
        
        for num in nums:
            if num == 0:
                end0 = (2 * end0 + 1) % MOD
            elif num == 1:
                end1 = (2 * end1 + end0) % MOD
            elif num == 2:
                end2 = (2 * end2 + end1) % MOD
        
        return end2

def countSpecialSubsequences(nums: List[int]) -> int:
    return Solution().countSpecialSubsequences(nums)