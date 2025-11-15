import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Function to find the maximum subarray sum using Kadane's algorithm
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        # Total sum of the array
        total_sum = sum(nums)
        
        # Maximum subarray sum using Kadane's algorithm
        max_kadane = kadane(nums)
        
        # Invert the array to find the minimum subarray sum
        inverted_nums = [-x for x in nums]
        min_kadane = kadane(inverted_nums)
        
        # Maximum subarray sum in the circular case
        max_circular = total_sum + min_kadane
        
        # If all numbers are negative, max_kadane will be the answer
        # Otherwise, we take the maximum of max_kadane and max_circular
        return max(max_kadane, max_circular) if max_circular != 0 else max_kadane

def maxSubarraySumCircular(nums: List[int]) -> int:
    return Solution().maxSubarraySumCircular(nums)