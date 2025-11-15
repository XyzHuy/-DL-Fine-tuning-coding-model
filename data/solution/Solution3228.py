import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxOperations(self, s: str) -> int:
        ans = cnt = 0
        for i, c in enumerate(s):
            if c == "1":
                cnt += 1
            elif i and s[i - 1] == "1":
                ans += cnt
        return ans

def maxOperations(s: str) -> int:
    return Solution().maxOperations(s)