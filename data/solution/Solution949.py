import random
import functools
import collections
import string
import math
import datetime


from itertools import permutations
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # Generate all possible permutations of the array
        max_time = -1
        for perm in permutations(arr):
            # Extract hours and minutes from the permutation
            hours = perm[0] * 10 + perm[1]
            minutes = perm[2] * 10 + perm[3]
            
            # Check if the permutation forms a valid time
            if 0 <= hours < 24 and 0 <= minutes < 60:
                total_minutes = hours * 60 + minutes
                max_time = max(max_time, total_minutes)
        
        # If no valid time was found, return an empty string
        if max_time == -1:
            return ""
        
        # Format the largest time found as "HH:MM"
        return "{:02}:{:02}".format(max_time // 60, max_time % 60)

def largestTimeFromDigits(arr: List[int]) -> str:
    return Solution().largestTimeFromDigits(arr)