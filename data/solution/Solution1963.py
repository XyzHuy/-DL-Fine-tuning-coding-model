import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minSwaps(self, s: str) -> int:
        x = 0
        for c in s:
            if c == "[":
                x += 1
            elif x:
                x -= 1
        return (x + 1) >> 1

def minSwaps(s: str) -> int:
    return Solution().minSwaps(s)