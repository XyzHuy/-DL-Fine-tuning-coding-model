import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        # Iterate over all possible quadruplets
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count

def countQuadruplets(nums: List[int]) -> int:
    return Solution().countQuadruplets(nums)