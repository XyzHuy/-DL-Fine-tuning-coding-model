import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of a count
        count_index_map = {0: -1}
        max_length = 0
        count = 0
        
        for i, num in enumerate(nums):
            # Increment count for 1, decrement for 0
            if num == 1:
                count += 1
            else:
                count -= 1
            
            # If the count has been seen before, calculate the subarray length
            if count in count_index_map:
                max_length = max(max_length, i - count_index_map[count])
            else:
                # Store the first occurrence of the count
                count_index_map[count] = i
        
        return max_length

def findMaxLength(nums: List[int]) -> int:
    return Solution().findMaxLength(nums)