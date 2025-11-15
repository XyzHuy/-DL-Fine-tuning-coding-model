import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

def peakIndexInMountainArray(arr: List[int]) -> int:
    return Solution().peakIndexInMountainArray(arr)