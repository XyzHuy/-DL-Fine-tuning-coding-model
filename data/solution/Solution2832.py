import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        next_greater = [n] * n
        prev_greater = [-1] * n
        
        # Find the next greater element for each element
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = i
            stack.append(i)
        
        # Find the previous greater element for each element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                prev_greater[stack.pop()] = i
            stack.append(i)
        
        # Calculate the maximum length of ranges
        ans = [0] * n
        for i in range(n):
            ans[i] = next_greater[i] - prev_greater[i] - 1
        
        return ans

def maximumLengthOfRanges(nums: List[int]) -> List[int]:
    return Solution().maximumLengthOfRanges(nums)