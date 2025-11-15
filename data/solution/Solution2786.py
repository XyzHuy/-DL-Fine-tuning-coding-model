import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # Initialize two variables to keep track of the maximum score ending with an even number and an odd number
        max_even = -float('inf')
        max_odd = -float('inf')
        
        # Determine the starting point based on the parity of the first element
        if nums[0] % 2 == 0:
            max_even = nums[0]
        else:
            max_odd = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            if num % 2 == 0:
                # If the current number is even, we can either take it from the previous even or odd score
                max_even = num + max(max_even, max_odd - x)
            else:
                # If the current number is odd, we can either take it from the previous even or odd score
                max_odd = num + max(max_even - x, max_odd)
        
        # The result will be the maximum score we can achieve, either ending with an even or odd number
        return max(max_even, max_odd)

def maxScore(nums: List[int], x: int) -> int:
    return Solution().maxScore(nums, x)