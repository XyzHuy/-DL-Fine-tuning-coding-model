import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            l, r = 0, len(g)
            while l < r:
                mid = (l + r) >> 1
                if g[mid] < x:
                    r = mid
                else:
                    l = mid + 1
            if l == len(g):
                g.append(x)
            else:
                g[l] = x
        return len(g)

# Example usage:
# sol = Solution()
# print(sol.minOperations([5, 3, 1, 4, 2]))  # Output: 3
# print(sol.minOperations([1, 2, 3, 4, 5]))  # Output: 1
# print(sol.minOperations([5, 4, 3, 2, 1]))  # Output: 5

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)