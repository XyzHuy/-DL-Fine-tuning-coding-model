import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # Initialize the sorted list to keep track of negative numbers in the current window
        window = SortedList()
        result = []
        
        # Process the first window
        for i in range(k):
            if nums[i] < 0:
                window.add(nums[i])
        
        # Determine the beauty of the first window
        if len(window) >= x:
            result.append(window[x - 1])
        else:
            result.append(0)
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Add the new element to the window if it is negative
            if nums[i] < 0:
                window.add(nums[i])
            
            # Remove the element that is sliding out of the window if it is negative
            if nums[i - k] < 0:
                window.remove(nums[i - k])
            
            # Determine the beauty of the current window
            if len(window) >= x:
                result.append(window[x - 1])
            else:
                result.append(0)
        
        return result

def getSubarrayBeauty(nums: List[int], k: int, x: int) -> List[int]:
    return Solution().getSubarrayBeauty(nums, k, x)