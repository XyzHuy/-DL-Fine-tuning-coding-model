import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(L: int, M: int) -> int:
            # Calculate prefix sums
            prefix_sum = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
            # Initialize the maximum sum for the first subarray of length L
            max_L = 0
            result = 0
            
            # Iterate over all possible positions for the first subarray of length L
            for i in range(len(nums) - L - M + 1):
                # Calculate the sum of the current subarray of length L
                L_sum = prefix_sum[i + L] - prefix_sum[i]
                # Update the maximum sum of any subarray of length L seen so far
                max_L = max(max_L, L_sum)
                # Calculate the sum of the current subarray of length M
                M_sum = prefix_sum[i + L + M] - prefix_sum[i + L]
                # Update the result with the maximum sum of the two non-overlapping subarrays
                result = max(result, max_L + M_sum)
            
            return result
        
        # Calculate the maximum sum for both possible orders of subarrays
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))

def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
    return Solution().maxSumTwoNoOverlap(nums, firstLen, secondLen)