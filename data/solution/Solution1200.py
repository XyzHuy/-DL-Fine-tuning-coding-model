import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array to make it easier to find minimum absolute differences
        arr.sort()
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        # List to store the pairs with the minimum absolute difference
        result = []
        
        # Find the minimum absolute difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    return Solution().minimumAbsDifference(arr)