import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        count = 0
        for num in num_counts:
            if k == 0:
                if num_counts[num] > 1:
                    count += 1
            else:
                if num + k in num_counts:
                    count += 1
        
        return count

def findPairs(nums: List[int], k: int) -> int:
    return Solution().findPairs(nums, k)