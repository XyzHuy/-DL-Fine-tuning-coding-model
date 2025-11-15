import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, used):
            if pos == n + 1:
                return 1
            count = 0
            for i in range(1, n + 1):
                if not used[i] and (pos % i == 0 or i % pos == 0):
                    used[i] = True
                    count += backtrack(pos + 1, used)
                    used[i] = False
            return count
        
        used = [False] * (n + 1)
        return backtrack(1, used)

def countArrangement(n: int) -> int:
    return Solution().countArrangement(n)