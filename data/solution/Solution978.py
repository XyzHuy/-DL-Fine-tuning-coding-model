import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        
        max_length = 1
        current_length = 1
        last_was_gt = None
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if last_was_gt is None or last_was_gt is False:
                    current_length += 1
                    last_was_gt = True
                else:
                    current_length = 2
                    last_was_gt = True
            elif arr[i] < arr[i - 1]:
                if last_was_gt is None or last_was_gt is True:
                    current_length += 1
                    last_was_gt = False
                else:
                    current_length = 2
                    last_was_gt = False
            else:
                current_length = 1
                last_was_gt = None
            
            max_length = max(max_length, current_length)
        
        return max_length

def maxTurbulenceSize(arr: List[int]) -> int:
    return Solution().maxTurbulenceSize(arr)