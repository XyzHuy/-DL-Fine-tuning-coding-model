import random
import functools
import collections
import string
import math
import datetime


from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            if k == 1:
                return s1[i] == s2[j]
            for h in range(1, k):
                if dfs(i, j, h) and dfs(i + h, j + h, k - h):
                    return True
                if dfs(i + h, j, k - h) and dfs(i, j + k - h, h):
                    return True
            return False

        return dfs(0, 0, len(s1))

def isScramble(s1: str, s2: str) -> bool:
    return Solution().isScramble(s1, s2)