import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize the current number and the index for arr
        current = 1
        index = 0
        
        # Iterate until we find the kth missing number
        while k > 0:
            # If the current number is not in the array, it's missing
            if index >= len(arr) or current != arr[index]:
                k -= 1
            else:
                # If the current number is in the array, move to the next number in the array
                index += 1
            # Move to the next positive number
            current += 1
        
        # Since we incremented current one step after finding the kth missing number
        return current - 1

def findKthPositive(arr: List[int], k: int) -> int:
    return Solution().findKthPositive(arr, k)