import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: d.get(x, 0)))


def customSortString(order: str, s: str) -> str:
    return Solution().customSortString(order, s)