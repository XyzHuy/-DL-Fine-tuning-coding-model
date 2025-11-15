import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] + nums[k]) % d == 0:
                        count += 1
        return count

def divisibleTripletCount(nums: List[int], d: int) -> int:
    return Solution().divisibleTripletCount(nums, d)