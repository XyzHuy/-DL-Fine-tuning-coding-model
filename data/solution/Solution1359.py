import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        count = 1
        for i in range(2, n + 1):
            count = count * i * (2 * i - 1) % MOD
        return count

def countOrders(n: int) -> int:
    return Solution().countOrders(n)