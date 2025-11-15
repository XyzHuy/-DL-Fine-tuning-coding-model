import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = float('inf')
        unique_vals = set()
        
        for r in range(len(arr)):
            # Update the set with the bitwise AND of the current subarray
            unique_vals = {arr[r] & val for val in unique_vals} | {arr[r]}
            # Find the minimum difference
            res = min(res, min(abs(val - target) for val in unique_vals))
        
        return res

def closestToTarget(arr: List[int], target: int) -> int:
    return Solution().closestToTarget(arr, target)