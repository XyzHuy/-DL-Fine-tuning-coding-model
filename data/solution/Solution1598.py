import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for v in logs:
            if v == "../":
                ans = max(0, ans - 1)
            elif v[0] != ".":
                ans += 1
        return ans

def minOperations(logs: List[str]) -> int:
    return Solution().minOperations(logs)