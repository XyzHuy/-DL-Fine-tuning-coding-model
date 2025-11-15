import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1  # Adjust k to be zero-indexed

        while k > 0:
            count = self.getCntNodes(current, n)
            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1
        return current

    def getCntNodes(self, current: int, n: int) -> int:
        nxt = current + 1
        totalNodes = 0
        while current <= n:
            totalNodes += min(n - current + 1, nxt - current)
            current *= 10
            nxt *= 10
        return totalNodes

def findKthNumber(n: int, k: int) -> int:
    return Solution().findKthNumber(n, k)