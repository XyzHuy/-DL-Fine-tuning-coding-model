import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count

def numOfPairs(nums: List[str], target: str) -> int:
    return Solution().numOfPairs(nums, target)