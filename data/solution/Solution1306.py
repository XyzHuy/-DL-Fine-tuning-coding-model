import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = [start]
        
        while queue:
            i = queue.pop(0)
            if i < 0 or i >= n or visited[i]:
                continue
            if arr[i] == 0:
                return True
            visited[i] = True
            queue.append(i + arr[i])
            queue.append(i - arr[i])
        
        return False

def canReach(arr: List[int], start: int) -> bool:
    return Solution().canReach(arr, start)