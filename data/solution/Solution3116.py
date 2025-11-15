import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def lcm_multiple(numbers):
            return reduce(lcm, numbers)
        
        def count_multiples(limit):
            count = 0
            for i in range(1, 1 << len(coins)):
                current_lcm = 1
                sign = -1
                for j in range(len(coins)):
                    if i & (1 << j):
                        current_lcm = lcm_multiple([current_lcm, coins[j]])
                        sign *= -1
                count += sign * (limit // current_lcm)
            return count
        
        low, high = 1, 2 * 10**9
        while low < high:
            mid = (low + high) // 2
            if count_multiples(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

def findKthSmallest(coins: List[int], k: int) -> int:
    return Solution().findKthSmallest(coins, k)