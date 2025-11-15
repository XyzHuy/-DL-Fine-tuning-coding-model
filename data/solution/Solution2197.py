import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            while stack:
                prev = stack[-1]
                current_gcd = gcd(prev, num)
                if current_gcd == 1:
                    break
                num = (prev * num) // current_gcd
                stack.pop()
            stack.append(num)
        
        return stack

def replaceNonCoprimes(nums: List[int]) -> List[int]:
    return Solution().replaceNonCoprimes(nums)