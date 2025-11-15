import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * n
        
        # Calculate the frequency of each index being requested
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        # Compute the prefix sum to get the actual frequency of each index
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        # Sort the frequency and the nums array
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        # Calculate the maximum sum by pairing the highest frequency with the largest number
        max_sum = sum(f * num for f, num in zip(freq, nums)) % MOD
        
        return max_sum

def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    return Solution().maxSumRangeQuery(nums, requests)