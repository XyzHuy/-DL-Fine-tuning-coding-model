import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect
import functools

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()  # Sort arr2 to use binary search for the next greater element

        @functools.lru_cache(None)
        def dp(i, prev):
            if i == len(arr1):
                return 0  # No more elements to process, return 0 operations

            # Option 1: Do not replace arr1[i], only if it is greater than prev
            if arr1[i] > prev:
                result = dp(i + 1, arr1[i])
            else:
                result = float('inf')  # Set to infinity if not possible

            # Option 2: Replace arr1[i] with the smallest element in arr2 that is greater than prev
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                result = min(result, 1 + dp(i + 1, arr2[idx]))

            return result

        result = dp(0, -1)
        return result if result != float('inf') else -1

def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
    return Solution().makeArrayIncreasing(arr1, arr2)