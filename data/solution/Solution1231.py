import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canDivide(minSweet):
            total = 0
            pieces = 0
            for sweet in sweetness:
                total += sweet
                if total >= minSweet:
                    pieces += 1
                    total = 0
            return pieces >= k + 1
        
        left, right = min(sweetness), sum(sweetness) // (k + 1)
        best = 0
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best

def maximizeSweetness(sweetness: List[int], k: int) -> int:
    return Solution().maximizeSweetness(sweetness, k)