import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        jumps = [1] * n  # jumps[i] will hold the maximum number of jumps starting from index i
        
        # Sort indices based on the value in arr, we will process smaller values first
        indices = sorted(range(n), key=lambda i: arr[i])
        
        for i in indices:
            # Try to jump to the left
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                jumps[i] = max(jumps[i], jumps[j] + 1)
            
            # Try to jump to the right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                jumps[i] = max(jumps[i], jumps[j] + 1)
        
        return max(jumps)

def maxJumps(arr: List[int], d: int) -> int:
    return Solution().maxJumps(arr, d)