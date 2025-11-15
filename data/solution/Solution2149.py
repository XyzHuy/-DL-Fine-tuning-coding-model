import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i, j = 0, 1
        for x in nums:
            if x > 0:
                ans[i] = x
                i += 2
            else:
                ans[j] = x
                j += 2
        return ans

def rearrangeArray(nums: List[int]) -> List[int]:
    return Solution().rearrangeArray(nums)