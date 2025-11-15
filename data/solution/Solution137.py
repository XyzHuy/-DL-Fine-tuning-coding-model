import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = sum(num >> i & 1 for num in nums)
            if cnt % 3:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans

def singleNumber(nums: List[int]) -> int:
    return Solution().singleNumber(nums)