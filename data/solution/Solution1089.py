import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                # Insert a zero at the next position
                arr.insert(i + 1, 0)
                # Skip the next element as it is the inserted zero
                i += 2
            else:
                i += 1
        # If the array has grown beyond its original length, truncate it
        arr[:] = arr[:n]

def duplicateZeros(arr: List[int]) -> None:
    return Solution().duplicateZeros(arr)