import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = [n - bisect_right(row[::-1], 0) for row in mat]
        idx = list(range(m))
        idx.sort(key=lambda i: (ans[i], i))
        return idx[:k]

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    return Solution().kWeakestRows(mat, k)