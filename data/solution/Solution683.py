import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
        
        # Initialize the result to a large number
        result = float('inf')
        # Use two pointers to find the valid slots
        left, right = 0, k + 1
        
        while right < n:
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                result = min(result, max(days[left], days[right]))
                left, right = right, right + k + 1
        
        return result if result != float('inf') else -1

def kEmptySlots(bulbs: List[int], k: int) -> int:
    return Solution().kEmptySlots(bulbs, k)