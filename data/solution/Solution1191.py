import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Helper function to find the maximum sub-array sum using Kadane's Algorithm
        def max_subarray_sum(arr):
            max_ending_here = max_so_far = 0
            for x in arr:
                max_ending_here = max(0, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        # Single array max sub-array sum
        max_kadane = max_subarray_sum(arr)
        
        # Sum of the entire array
        total_sum = sum(arr)
        
        if k == 1:
            return max_kadane % MOD
        
        # Max sub-array sum for two concatenated arrays
        max_two_concat = max_subarray_sum(arr + arr)
        
        if total_sum > 0:
            # If the total sum of arr is positive, consider the max sum with k concatenations
            return max(max_kadane, max_two_concat, total_sum * (k - 2) + max_two_concat) % MOD
        else:
            # If the total sum is non-positive, only consider up to two concatenations
            return max(max_kadane, max_two_concat) % MOD

def kConcatenationMaxSum(arr: List[int], k: int) -> int:
    return Solution().kConcatenationMaxSum(arr, k)