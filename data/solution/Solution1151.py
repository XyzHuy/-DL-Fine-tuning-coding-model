import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Count the total number of 1's in the array
        total_ones = sum(data)
        
        # If there are 0 or 1 ones, no swaps are needed
        if total_ones <= 1:
            return 0
        
        # Initialize the maximum number of 1's in any window of size total_ones
        max_ones_in_window = 0
        
        # Initialize the first window
        for i in range(total_ones):
            if data[i] == 1:
                max_ones_in_window += 1
        
        # Slide the window across the array
        current_ones_in_window = max_ones_in_window
        for i in range(total_ones, len(data)):
            current_ones_in_window += data[i] - data[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        # The minimum number of swaps is the total number of 1's minus the maximum number of 1's in any window
        return total_ones - max_ones_in_window

def minSwaps(data: List[int]) -> int:
    return Solution().minSwaps(data)