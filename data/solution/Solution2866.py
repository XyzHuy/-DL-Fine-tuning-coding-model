import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        
        # Function to calculate the prefix sums using monotonic stack
        def calculate_sums(arr):
            stack = []
            sums = [0] * n
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    sums[i] = sums[stack[-1]] + arr[i] * (i - stack[-1])
                else:
                    sums[i] = arr[i] * (i + 1)
                stack.append(i)
            return sums
        
        # Calculate prefix sums for non-decreasing left part
        left_sums = calculate_sums(maxHeights)
        
        # Calculate suffix sums for non-increasing right part
        right_sums = calculate_sums(maxHeights[::-1])[::-1]
        
        # Find the maximum sum of heights for a beautiful configuration
        max_sum = 0
        for i in range(n):
            # Total sum for peak at i
            total_sum = left_sums[i] + right_sums[i] - maxHeights[i]
            max_sum = max(max_sum, total_sum)
        
        return max_sum

def maximumSumOfHeights(maxHeights: List[int]) -> int:
    return Solution().maximumSumOfHeights(maxHeights)