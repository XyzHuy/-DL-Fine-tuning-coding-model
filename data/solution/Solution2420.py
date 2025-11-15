import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 2 * k + 1:
            return []

        # Arrays to store the length of non-increasing and non-decreasing subarrays
        non_increasing = [1] * n
        non_decreasing = [1] * n

        # Fill non_increasing array
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1

        # Fill non_decreasing array
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1

        # Find good indices
        good_indices = []
        for i in range(k, n - k):
            if non_increasing[i - 1] >= k and non_decreasing[i + 1] >= k:
                good_indices.append(i)

        return good_indices

def goodIndices(nums: List[int], k: int) -> List[int]:
    return Solution().goodIndices(nums, k)