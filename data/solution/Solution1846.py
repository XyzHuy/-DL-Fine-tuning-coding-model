import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # First, sort the array
        arr.sort()
        
        # Ensure the first element is 1
        arr[0] = 1
        
        # Iterate through the array and adjust elements to satisfy the conditions
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        
        # The maximum element in the modified array is the answer
        return arr[-1]

def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
    return Solution().maximumElementAfterDecrementingAndRearranging(arr)