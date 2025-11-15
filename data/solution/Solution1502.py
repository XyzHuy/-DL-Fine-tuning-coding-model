import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array
        arr.sort()
        
        # Calculate the common difference
        common_difference = arr[1] - arr[0]
        
        # Check if all consecutive elements have the same difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != common_difference:
                return False
        
        return True

def canMakeArithmeticProgression(arr: List[int]) -> bool:
    return Solution().canMakeArithmeticProgression(arr)