import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, diff):
            if i == len(s1) and j == len(s2):
                return diff == 0
            
            if i < len(s1) and s1[i].isdigit():
                num = 0
                for k in range(i, min(i + 3, len(s1))):
                    if not s1[k].isdigit():
                        break
                    num = num * 10 + int(s1[k])
                    if dfs(k + 1, j, diff - num):
                        return True
            elif j < len(s2) and s2[j].isdigit():
                num = 0
                for k in range(j, min(j + 3, len(s2))):
                    if not s2[k].isdigit():
                        break
                    num = num * 10 + int(s2[k])
                    if dfs(i, k + 1, diff + num):
                        return True
            elif diff > 0 and i < len(s1):
                if dfs(i + 1, j, diff - 1):
                    return True
            elif diff < 0 and j < len(s2):
                if dfs(i, j + 1, diff + 1):
                    return True
            elif diff == 0 and i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                if dfs(i + 1, j + 1, 0):
                    return True
            return False

        return dfs(0, 0, 0)

def possiblyEquals(s1: str, s2: str) -> bool:
    return Solution().possiblyEquals(s1, s2)