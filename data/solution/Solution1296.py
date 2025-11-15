import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        count = Counter(nums)
        for n in sorted(count):
            if count[n] > 0:
                needed = count[n]
                for i in range(n, n + k):
                    if count[i] < needed:
                        return False
                    count[i] -= needed
        
        return True

def isPossibleDivide(nums: List[int], k: int) -> bool:
    return Solution().isPossibleDivide(nums, k)