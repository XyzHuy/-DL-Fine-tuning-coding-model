import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count the frequency of elements in the current window
        frequency = defaultdict(int)
        # Result list to store the count of distinct elements for each window
        result = []
        
        # Initialize the first window
        for i in range(k):
            frequency[nums[i]] += 1
        
        # The number of distinct elements in the first window
        result.append(len(frequency))
        
        # Slide the window over the array
        for i in range(k, len(nums)):
            # Add the new element to the window
            frequency[nums[i]] += 1
            # Remove the element that is left out of the window
            frequency[nums[i - k]] -= 1
            
            # If the count of the removed element becomes zero, remove it from the dictionary
            if frequency[nums[i - k]] == 0:
                del frequency[nums[i - k]]
            
            # Append the number of distinct elements in the current window to the result
            result.append(len(frequency))
        
        return result

def distinctNumbers(nums: List[int], k: int) -> List[int]:
    return Solution().distinctNumbers(nums, k)