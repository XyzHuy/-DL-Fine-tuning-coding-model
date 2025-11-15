import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n  # previous smaller element's index
        right = [n] * n  # next smaller element's index
        
        # Monotonic stack to find the previous smaller element
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # Monotonic stack to find the next smaller element
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        # Frequency array to count the maximum possible minimum values for each subarray length
        freq = [0] * (n + 1)
        for i in range(n):
            length = right[i] - left[i] - 1
            freq[length] = max(freq[length], nums[i])
        
        # Fill the frequency array to ensure the maximum values are propagated correctly
        for i in range(n - 1, 0, -1):
            freq[i] = max(freq[i], freq[i + 1])
        
        # Construct the result array
        result = [0] * n
        for i in range(n):
            result[i] = freq[i + 1]
        
        return result

def findMaximums(nums: List[int]) -> List[int]:
    return Solution().findMaximums(nums)