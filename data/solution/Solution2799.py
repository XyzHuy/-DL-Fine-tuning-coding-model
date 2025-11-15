import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct_count = len(set(nums))
        n = len(nums)
        count = 0
        
        for start in range(n):
            current_count = Counter()
            distinct_count = 0
            
            for end in range(start, n):
                if current_count[nums[end]] == 0:
                    distinct_count += 1
                current_count[nums[end]] += 1
                
                if distinct_count == total_distinct_count:
                    count += (n - end)
                    break
        
        return count

def countCompleteSubarrays(nums: List[int]) -> int:
    return Solution().countCompleteSubarrays(nums)