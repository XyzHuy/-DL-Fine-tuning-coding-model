import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Sort the nums array
        nums.sort()
        
        # Initialize the averages list
        averages = []
        
        # Repeat the procedure n / 2 times
        n = len(nums)
        for i in range(n // 2):
            # Remove the smallest element (minElement) and the largest element (maxElement)
            minElement = nums.pop(0)
            maxElement = nums.pop(-1)
            
            # Add (minElement + maxElement) / 2 to averages
            averages.append((minElement + maxElement) / 2)
        
        # Return the minimum element in averages
        return min(averages)

def minimumAverage(nums: List[int]) -> float:
    return Solution().minimumAverage(nums)