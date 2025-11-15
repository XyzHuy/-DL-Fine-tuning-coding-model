import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Find the longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the entire array is non-decreasing
        if left == n - 1:
            return 0
        
        # Find the longest non-decreasing suffix
        right = n - 1
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Option 1: Remove the middle part, keeping the left prefix
        result = min(n - left - 1, right)
        
        # Option 2: Try to connect the left prefix with the right suffix
        i, j = 0, right
        while i <= left and j <= n - 1:
            if arr[i] <= arr[j]:
                # We can connect arr[0:i+1] + arr[j:]
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result

def findLengthOfShortestSubarray(arr: List[int]) -> int:
    return Solution().findLengthOfShortestSubarray(arr)