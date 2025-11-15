import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0
        
        for num in count:
            if count[num] > 0:
                complement = k - num
                if complement == num:
                    # If the number and its complement are the same, we can form pairs within the same number
                    operations += count[num] // 2
                    count[num] = count[num] % 2
                elif complement in count and count[complement] > 0:
                    # Form a pair with the complement
                    operations += min(count[num], count[complement])
                    count[num] = 0
                    count[complement] -= min(count[num], count[complement])
        
        return operations

def maxOperations(nums: List[int], k: int) -> int:
    return Solution().maxOperations(nums, k)