import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            # Start by printing s[i] from i to j
            result = 1 + dp(i + 1, j)
            # Try to merge the print job by finding any s[k] == s[i]
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    result = min(result, dp(i, k - 1) + dp(k + 1, j))
            return result

        return dp(0, len(s) - 1)

def strangePrinter(s: str) -> int:
    return Solution().strangePrinter(s)