import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        perm = list(range(1, n + 1))
        i = 0
        while i < n - 1:
            if s[i] == 'D':
                start = i
                while i < n - 1 and s[i] == 'D':
                    i += 1
                perm[start:i+1] = reversed(perm[start:i+1])
            else:
                i += 1
        return perm

def findPermutation(s: str) -> List[int]:
    return Solution().findPermutation(s)