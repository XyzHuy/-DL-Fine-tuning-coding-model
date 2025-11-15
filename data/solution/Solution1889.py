import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        n = len(packages)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]
        
        min_waste = float('inf')
        for box in boxes:
            if max(box) < max(packages):
                continue
            box.sort()
            current_waste = 0
            j = 0
            for size in box:
                i = bisect_right(packages, size)
                if i > j:
                    current_waste += (i - j) * size - (prefix_sum[i] - prefix_sum[j])
                    j = i
            min_waste = min(min_waste, current_waste)
        
        return min_waste % (10**9 + 7) if min_waste != float('inf') else -1

def minWastedSpace(packages: List[int], boxes: List[List[int]]) -> int:
    return Solution().minWastedSpace(packages, boxes)