import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        count = 0
        
        for num in nums:
            # Maintain the stack such that the elements are in non-decreasing order
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            # The number of valid subarrays ending at the current element
            count += len(stack)
        
        return count

def validSubarrays(nums: List[int]) -> int:
    return Solution().validSubarrays(nums)