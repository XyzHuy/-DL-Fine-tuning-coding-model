import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Count the occurrences of each element in arr1
        count = Counter(arr1)
        
        # Initialize the result array
        result = []
        
        # Add elements from arr1 that are in arr2, in the order they appear in arr2
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        # Add the remaining elements from arr1 that are not in arr2, in ascending order
        for num in sorted(count):
            result.extend([num] * count[num])
        
        return result

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    return Solution().relativeSortArray(arr1, arr2)