import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        
        return n - left

def hIndex(citations: List[int]) -> int:
    return Solution().hIndex(citations)