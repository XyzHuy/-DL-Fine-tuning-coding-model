import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Calculate the target sum for sub-arrays of size k
        target_sum = k * threshold
        
        # Initialize the sum of the first sub-array of size k
        current_sum = sum(arr[:k])
        
        # Initialize the count of valid sub-arrays
        count = 1 if current_sum >= target_sum else 0
        
        # Use sliding window to find all sub-arrays of size k
        for i in range(k, len(arr)):
            # Slide the window: subtract the element going out and add the element coming in
            current_sum += arr[i] - arr[i - k]
            
            # Check if the current sub-array meets the condition
            if current_sum >= target_sum:
                count += 1
        
        return count

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    return Solution().numOfSubarrays(arr, k, threshold)