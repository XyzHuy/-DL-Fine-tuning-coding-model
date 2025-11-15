import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        i = 1
        
        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Find the left boundary of the mountain
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                # Find the right boundary of the mountain
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                # Calculate the length of the mountain
                max_length = max(max_length, right - left + 1)
                
                # Move the index to the end of the current mountain
                i = right
            else:
                i += 1
        
        return max_length

def longestMountain(arr: List[int]) -> int:
    return Solution().longestMountain(arr)