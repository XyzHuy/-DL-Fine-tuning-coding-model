import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # This will keep track of the potential '3' in the 132 pattern
        third = float('-inf')
        # This stack will be used to keep elements that could be '3' candidates
        stack = []
        
        # Traverse the array from the end to the start
        for num in reversed(nums):
            # Check if we can find a valid '1'
            if num < third:
                return True
            
            # Maintain the stack to find a valid '3'
            while stack and stack[-1] < num:
                third = stack.pop()
            
            # Push the current number as a potential '3'
            stack.append(num)
        
        return False

def find132pattern(nums: List[int]) -> bool:
    return Solution().find132pattern(nums)