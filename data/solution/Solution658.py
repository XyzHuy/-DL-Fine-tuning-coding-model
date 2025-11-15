import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find the position to insert x to keep the array sorted
        insert_pos = bisect.bisect_left(arr, x)
        
        # Initialize two pointers
        left = max(0, insert_pos - k)
        right = min(len(arr) - 1, insert_pos + k - 1)
        
        # Use binary search to find the k closest elements
        while right - left > k - 1:
            if left < 0 or (x - arr[left]) <= (arr[right] - x):
                right -= 1
            elif right > len(arr) - 1 or (x - arr[left]) > (arr[right] - x):
                left += 1
        
        return arr[left:right + 1]

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    return Solution().findClosestElements(arr, k, x)