import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Dictionary to store the maximum length of subsequence ending with a number
        # having a specific remainder when added to the previous number in the subsequence
        dp = {}

        max_length = 1

        for i in range(len(nums)):
            for j in range(i):
                remainder = (nums[i] + nums[j]) % k
                if (j, remainder) in dp:
                    dp[(i, remainder)] = dp[(j, remainder)] + 1
                    max_length = max(max_length, dp[(i, remainder)])
                else:
                    dp[(i, remainder)] = 2
                    max_length = max(max_length, dp[(i, remainder)])

        return max_length

def maximumLength(nums: List[int], k: int) -> int:
    return Solution().maximumLength(nums, k)