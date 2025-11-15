import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                first_digit = int(str(nums[i])[0])
                last_digit = int(str(nums[j])[-1])
                if gcd(first_digit, last_digit) == 1:
                    count += 1
        
        return count

def countBeautifulPairs(nums: List[int]) -> int:
    return Solution().countBeautifulPairs(nums)