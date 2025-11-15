import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def newInteger(self, n: int) -> int:
        ans = []
        while n:
            ans.append(str(n % 9))
            n //= 9
        return ''.join(reversed(ans))

def newInteger(n: int) -> int:
    return Solution().newInteger(n)