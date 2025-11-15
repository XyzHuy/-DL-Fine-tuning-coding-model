import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0
        
        for k in range(len(arr)):
            for j in range(k):
                i = index_map.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_length = max(max_length, dp[(j, k)])
        
        return max_length if max_length >= 3 else 0

def lenLongestFibSubseq(arr: List[int]) -> int:
    return Solution().lenLongestFibSubseq(arr)