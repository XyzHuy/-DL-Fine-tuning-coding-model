import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Identify the dominant element
        count = Counter(nums)
        total_length = len(nums)
        dominant_element = None
        dominant_count = 0
        
        for num, cnt in count.items():
            if cnt * 2 > total_length:
                dominant_element = num
                dominant_count = cnt
                break
        
        # Step 2: Count occurrences of the dominant element from left to right
        left_count = 0
        for i, num in enumerate(nums):
            if num == dominant_element:
                left_count += 1
                right_count = dominant_count - left_count
                left_length = i + 1
                right_length = total_length - left_length
                
                # Step 3: Check if the current split is valid
                if left_count * 2 > left_length and right_count * 2 > right_length:
                    return i
        
        # If no valid split is found, return -1
        return -1

def minimumIndex(nums: List[int]) -> int:
    return Solution().minimumIndex(nums)