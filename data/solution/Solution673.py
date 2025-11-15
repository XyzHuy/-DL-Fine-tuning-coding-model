import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        lengths = [1] * n  # lengths[i] will hold the length of the longest increasing subsequence ending at index i
        counts = [1] * n   # counts[i] will hold the number of longest increasing subsequences ending at index i
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        longest = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == longest)

def findNumberOfLIS(nums: List[int]) -> int:
    return Solution().findNumberOfLIS(nums)