import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = cnt = 1
        for i, x in enumerate(nums[1:]):
            if nums[i] < x:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans


def findLengthOfLCIS(nums: List[int]) -> int:
    return Solution().findLengthOfLCIS(nums)