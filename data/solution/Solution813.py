import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # Precompute the prefix sums to calculate the average of subarrays quickly
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Function to calculate the sum of subarray nums[left:right+1]
        def subarray_sum(left, right):
            return prefix_sum[right + 1] - prefix_sum[left]
        
        # Memoization dictionary
        memo = {}
        
        # Helper function to recursively calculate the maximum score
        def dp(start, partitions):
            if (start, partitions) in memo:
                return memo[(start, partitions)]
            
            # Base case: if there's only one partition left, return the average of the remaining subarray
            if partitions == 1:
                return subarray_sum(start, n - 1) / (n - start)
            
            max_score = 0
            # Try partitioning the array at every possible point
            for i in range(start, n - partitions + 1):
                current_avg = subarray_sum(start, i) / (i - start + 1)
                remaining_avg = dp(i + 1, partitions - 1)
                max_score = max(max_score, current_avg + remaining_avg)
            
            memo[(start, partitions)] = max_score
            return max_score
        
        # Start the recursion from the beginning of the array with k partitions
        return dp(0, k)

def largestSumOfAverages(nums: List[int], k: int) -> float:
    return Solution().largestSumOfAverages(nums, k)