import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_length = 0
        
        for i in range(n):
            if not visited[i]:
                current_length = 0
                k = i
                while not visited[k]:
                    visited[k] = True
                    k = nums[k]
                    current_length += 1
                max_length = max(max_length, current_length)
        
        return max_length

def arrayNesting(nums: List[int]) -> int:
    return Solution().arrayNesting(nums)