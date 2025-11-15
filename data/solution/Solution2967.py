import random
import functools
import collections
import string
import math
import datetime


from bisect import bisect_left
from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def f(x: int) -> int:
            return sum(abs(v - x) for v in nums)

        # Generate palindromic numbers up to 10^9
        ps = set()
        for i in range(1, 10**5 + 1):
            s = str(i)
            # Odd length palindromes
            ps.add(int(s + s[-2::-1]))
            # Even length palindromes
            ps.add(int(s + s[::-1]))
        ps = sorted(ps)

        # Sort the input list to find the median
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Find the closest palindromic numbers to the median
        i = bisect_left(ps, median)
        candidates = [ps[j] for j in range(i - 1, i + 2) if 0 <= j < len(ps)]
        
        # Calculate the minimum cost for each candidate
        return min(f(x) for x in candidates)

def minimumCost(nums: List[int]) -> int:
    return Solution().minimumCost(nums)