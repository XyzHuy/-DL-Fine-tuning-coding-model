import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        n = len(nums)
        m = len(queries)
        
        # Initialize the dp array
        f = [[0] * n for _ in range(n)]
        
        # Fill the dp array
        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                if i > 0:
                    f[i][j] = max(
                        f[i][j], f[i - 1][j] + (nums[i - 1] >= queries[f[i - 1][j]])
                    )
                if j + 1 < n:
                    f[i][j] = max(
                        f[i][j], f[i][j + 1] + (nums[j + 1] >= queries[f[i][j + 1]])
                    )
                if f[i][j] == m:
                    return m
        
        # Return the maximum value from the dp array considering the middle elements
        return max(f[i][i] + (nums[i] >= queries[f[i][i]]) for i in range(n))

def maximumProcessableQueries(nums: List[int], queries: List[int]) -> int:
    return Solution().maximumProcessableQueries(nums, queries)