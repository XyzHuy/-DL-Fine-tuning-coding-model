import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start, target):
            for i in range(start, int(target**0.5) + 1):
                if target % i == 0:
                    path.append(i)
                    res.append(path[:] + [target // i])
                    backtrack(i, target // i)
                    path.pop()
        
        res = []
        path = []
        backtrack(2, n)
        return res

def getFactors(n: int) -> List[List[int]]:
    return Solution().getFactors(n)