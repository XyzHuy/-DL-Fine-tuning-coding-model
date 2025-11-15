import random
import functools
import collections
import string
import math
import datetime


from functools import cache

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            # Option 1: Flip the i-th and j-th mismatched characters using the first operation
            a = dfs(i + 1, j - 1) + x
            # Option 2: Flip the i-th and (i+1)-th mismatched characters using the second operation
            b = dfs(i + 2, j) + idx[i + 1] - idx[i]
            # Option 3: Flip the (j-1)-th and j-th mismatched characters using the second operation
            c = dfs(i, j - 2) + idx[j] - idx[j - 1]
            return min(a, b, c)

        n = len(s1)
        # Collect indices where s1 and s2 differ
        idx = [i for i in range(n) if s1[i] != s2[i]]
        m = len(idx)
        # If the number of mismatched characters is odd, it's impossible to make the strings equal
        if m & 1:
            return -1
        return dfs(0, m - 1)

def minOperations(s1: str, s2: str, x: int) -> int:
    return Solution().minOperations(s1, s2, x)