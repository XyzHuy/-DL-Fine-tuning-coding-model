import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Calculate prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Monotonic increasing stack to find boundaries
        stack = []
        max_min_product = 0
        
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                min_index = stack.pop()
                left_bound = -1 if not stack else stack[-1]
                # Calculate the sum of the subarray from left_bound + 1 to i - 1
                total_sum = prefix_sum[i] - prefix_sum[left_bound + 1]
                # Calculate the min-product for the subarray
                min_product = nums[min_index] * total_sum
                max_min_product = max(max_min_product, min_product)
            stack.append(i)
        
        return max_min_product % MOD

def maxSumMinProduct(nums: List[int]) -> int:
    return Solution().maxSumMinProduct(nums)