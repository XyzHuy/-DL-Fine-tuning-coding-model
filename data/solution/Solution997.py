import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize in-degree and out-degree arrays
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        # Calculate in-degrees and out-degrees
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        
        # Find the judge
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        
        return -1

def findJudge(n: int, trust: List[List[int]]) -> int:
    return Solution().findJudge(n, trust)