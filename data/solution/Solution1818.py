import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        
        # Calculate the original absolute sum difference
        original_sum_diff = sum(abs(a - b) for a, b in zip(nums1, nums2))
        
        # Create a sorted copy of nums1 to use for binary search
        sorted_nums1 = sorted(nums1)
        
        # Initialize the maximum reduction in absolute sum difference
        max_reduction = 0
        
        # Iterate through each pair of elements
        for i in range(n):
            a, b = nums1[i], nums2[i]
            original_diff = abs(a - b)
            
            # Find the position to insert b in the sorted nums1
            pos = bisect.bisect_left(sorted_nums1, b)
            
            # Check the element at the found position and the element before it (if exists)
            for j in [pos, pos - 1]:
                if 0 <= j < n:
                    new_diff = abs(sorted_nums1[j] - b)
                    max_reduction = max(max_reduction, original_diff - new_diff)
        
        # Calculate the minimum possible sum difference after one replacement
        min_sum_diff = original_sum_diff - max_reduction
        
        # Return the result modulo 10^9 + 7
        return min_sum_diff % MOD

def minAbsoluteSumDiff(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minAbsoluteSumDiff(nums1, nums2)