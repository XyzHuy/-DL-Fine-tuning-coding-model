import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n  # Longest Increasing Subsequence ending at each index
        lds = [1] * n  # Longest Decreasing Subsequence starting at each index

        # Calculate LIS for each element
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        # Calculate LDS for each element
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        # Find the minimum removals to form a mountain array
        min_removals = n
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # Ensure it's a valid peak
                min_removals = min(min_removals, n - (lis[i] + lds[i] - 1))

        return min_removals

def minimumMountainRemovals(nums: List[int]) -> int:
    return Solution().minimumMountainRemovals(nums)