import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @lru_cache(None)
        def dp(index, mask):
            if index == n:
                return 0
            
            min_xor_sum = float('inf')
            for j in range(n):
                if not (mask & (1 << j)):
                    current_xor = nums1[index] ^ nums2[j]
                    min_xor_sum = min(min_xor_sum, current_xor + dp(index + 1, mask | (1 << j)))
            
            return min_xor_sum
        
        return dp(0, 0)

def minimumXORSum(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minimumXORSum(nums1, nums2)