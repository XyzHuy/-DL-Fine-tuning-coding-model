import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # Initialize variables to store the maximum sum of subarray without deletion
        # and with deletion ending at the current position
        max_ending_here = arr[0]
        max_ending_here_with_deletion = arr[0]
        max_so_far = arr[0]
        
        for i in range(1, n):
            # Update max_ending_here_with_deletion by either continuing the previous
            # subarray with deletion or starting a new subarray ending at i-1
            max_ending_here_with_deletion = max(max_ending_here, max_ending_here_with_deletion + arr[i])
            
            # Update max_ending_here by either continuing the previous subarray or starting a new one
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            
            # Update the overall maximum sum considering the current position
            max_so_far = max(max_so_far, max_ending_here, max_ending_here_with_deletion)
        
        return max_so_far

def maximumSum(arr: List[int]) -> int:
    return Solution().maximumSum(arr)