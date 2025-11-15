import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Calculate the sum of each subarray of length k
        n = len(nums)
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sums[0] = current_sum
        
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum
        
        # left[i] will be the index of the best subarray of length k in nums[0:i+1]
        left = [0] * (n - k + 1)
        best = 0
        for i in range(n - k + 1):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        
        # right[i] will be the index of the best subarray of length k in nums[i:]
        right = [0] * (n - k + 1)
        best = n - k
        for i in range(n - k, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best
        
        # Find the best combination of three subarrays
        max_sum = 0
        result = []
        for j in range(k, n - 2 * k + 1):
            i, l = left[j - k], right[j + k]
            total = sums[i] + sums[j] + sums[l]
            if total > max_sum:
                max_sum = total
                result = [i, j, l]
        
        return result

def maxSumOfThreeSubarrays(nums: List[int], k: int) -> List[int]:
    return Solution().maxSumOfThreeSubarrays(nums, k)