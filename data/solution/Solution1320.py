import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(c1, c2):
            if c1 is None:
                return 0
            x1, y1 = divmod(ord(c1) - ord('A'), 6)
            x2, y2 = divmod(ord(c2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0
            return min(dp(i + 1, word[i], f2) + dist(f1, word[i]),
                       dp(i + 1, f1, word[i]) + dist(f2, word[i]))
        
        return dp(0, None, None)

def minimumDistance(word: str) -> int:
    return Solution().minimumDistance(word)