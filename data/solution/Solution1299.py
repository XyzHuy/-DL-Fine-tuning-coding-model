import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initialize the maximum element to -1, which will be the value for the last element
        max_right = -1
        # Traverse the array from the end to the beginning
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element in a temporary variable
            current = arr[i]
            # Replace the current element with the maximum element to its right
            arr[i] = max_right
            # Update the maximum element to the right
            max_right = max(max_right, current)
        return arr

def replaceElements(arr: List[int]) -> List[int]:
    return Solution().replaceElements(arr)