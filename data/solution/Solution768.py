import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = float('-inf')
        chunks = 0
        
        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far <= min(arr[i+1:]) if i+1 < len(arr) else True:
                chunks += 1
        
        return chunks

def maxChunksToSorted(arr: List[int]) -> int:
    return Solution().maxChunksToSorted(arr)