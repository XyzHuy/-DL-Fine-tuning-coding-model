import random
import functools
import collections
import string
import math
import datetime


from itertools import accumulate
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        d = [0] * (k + 2)
        n = len(nums)
        for i in range(n // 2):
            x, y = nums[i], nums[-i - 1]
            if x > y:
                x, y = y, x
            d[0] += 1
            d[y - x] -= 1
            d[y - x + 1] += 1
            d[max(y, k - x) + 1] -= 1
            d[max(y, k - x) + 1] += 2
        return min(accumulate(d))

# Example usage:
# sol = Solution()
# print(sol.minChanges([1, 0, 1, 2, 4, 3], 4))  # Output: 2
# print(sol.minChanges([0, 1, 2, 3, 3, 6, 5, 4], 6))  # Output: 2

def minChanges(nums: List[int], k: int) -> int:
    return Solution().minChanges(nums, k)