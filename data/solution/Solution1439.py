import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pre = [0]
        for cur in mat:
            pre = sorted(a + b for a in pre for b in cur[:k])[:k]
        return pre[-1]

def kthSmallest(mat: List[List[int]], k: int) -> int:
    return Solution().kthSmallest(mat, k)