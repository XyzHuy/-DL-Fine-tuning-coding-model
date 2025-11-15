import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            # Create a copy of the array to store changes
            new_arr = arr[:]
            changed = False
            
            # Iterate over the array, except the first and last elements
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                    changed = True
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
                    changed = True
            
            # If no changes were made, return the array
            if not changed:
                return new_arr
            
            # Update arr to new_arr for the next iteration
            arr = new_arr

def transformArray(arr: List[int]) -> List[int]:
    return Solution().transformArray(arr)