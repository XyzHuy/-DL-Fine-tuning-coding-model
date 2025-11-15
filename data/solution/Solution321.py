import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(arr1, arr2):
            res = []
            while arr1 or arr2:
                bigger = arr1 if arr1 > arr2 else arr2
                res.append(bigger[0])
                bigger.pop(0)
            return res
        
        max_number = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                max_number = max(max_number, merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i)))
        
        return max_number

def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    return Solution().maxNumber(nums1, nums2, k)