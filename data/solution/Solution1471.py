import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # Sort the array to find the median
        arr.sort()
        n = len(arr)
        # The median is the middle element in the sorted array
        median = arr[(n - 1) // 2]
        
        # Sort the array based on the strength criteria
        # First by absolute difference from median, then by the value itself
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        
        # Return the first k elements from the sorted array
        return arr[:k]

def getStrongest(arr: List[int], k: int) -> List[int]:
    return Solution().getStrongest(arr, k)