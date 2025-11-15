import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        total_sum = 0
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                distinct_count = len(distinct_elements)
                total_sum = (total_sum + distinct_count * distinct_count) % MOD
        
        return total_sum

def sumCounts(nums: List[int]) -> int:
    return Solution().sumCounts(nums)