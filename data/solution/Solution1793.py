import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize the left and right pointers
        left = right = k
        # Initialize the minimum value in the current window
        min_val = nums[k]
        # Initialize the maximum score
        max_score = min_val
        
        # Expand the window while there are elements to consider
        while left > 0 or right < len(nums) - 1:
            # Expand the window to the left or right
            if (left == 0 or (right < len(nums) - 1 and nums[right + 1] > nums[left - 1])):
                right += 1
            else:
                left -= 1
            
            # Update the minimum value in the current window
            min_val = min(min_val, nums[left], nums[right])
            # Calculate the score of the current window and update the maximum score
            max_score = max(max_score, min_val * (right - left + 1))
        
        return max_score

def maximumScore(nums: List[int], k: int) -> int:
    return Solution().maximumScore(nums, k)