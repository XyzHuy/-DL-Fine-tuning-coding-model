import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n):
            return int(n**0.5) ** 2 == n
        
        def backtrack(path):
            if len(path) == len(nums):
                self.count += 1
                return
            
            for num in count:
                if count[num] > 0:
                    if not path or is_square(path[-1] + num):
                        count[num] -= 1
                        backtrack(path + [num])
                        count[num] += 1
        
        self.count = 0
        count = Counter(nums)
        backtrack([])
        return self.count

def numSquarefulPerms(nums: List[int]) -> int:
    return Solution().numSquarefulPerms(nums)