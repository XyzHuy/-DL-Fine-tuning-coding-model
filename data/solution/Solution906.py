import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(x: int) -> bool:
            y, t = 0, x
            while t:
                y = y * 10 + t % 10
                t //= 10
            return x == y

        l, r = int(left), int(right)
        ps = []
        for i in range(1, 10**5 + 1):
            s = str(i)
            t1 = s[::-1]
            t2 = s[:-1][::-1]
            ps.append(int(s + t1))
            ps.append(int(s + t2))

        return sum(l <= x <= r and is_palindrome(x) for x in map(lambda x: x * x, ps))

def superpalindromesInRange(left: str, right: str) -> int:
    return Solution().superpalindromesInRange(left, right)