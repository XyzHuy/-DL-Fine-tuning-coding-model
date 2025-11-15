import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Iterate over nums2 in reverse order
        for num in reversed(nums2):
            # Pop elements from the stack until we find a greater element
            while stack and stack[-1] <= num:
                stack.pop()
            # If stack is not empty, the top element is the next greater element
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            # Push the current element onto the stack
            stack.append(num)
        
        # Build the result for nums1 using the next_greater dictionary
        result = [next_greater[num] for num in nums1]
        return result

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().nextGreaterElement(nums1, nums2)