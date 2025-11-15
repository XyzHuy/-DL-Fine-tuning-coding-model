import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        distinct_subarrays = set()
        
        for start in range(n):
            count = 0
            for end in range(start, n):
                if nums[end] % p == 0:
                    count += 1
                if count > k:
                    break
                subarray = tuple(nums[start:end+1])
                distinct_subarrays.add(subarray)
        
        return len(distinct_subarrays)

def countDistinct(nums: List[int], k: int, p: int) -> int:
    return Solution().countDistinct(nums, k, p)