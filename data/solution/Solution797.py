import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            u = path[-1]
            if u == n - 1:
                ans.append(path)
                continue
            for v in graph[u]:
                q.append(path + [v])
        return ans

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    return Solution().allPathsSourceTarget(graph)