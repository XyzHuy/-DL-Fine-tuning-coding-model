import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def coloredCells(self, n: int) -> int:
        # Using the formula: 1 + 2 * n * (n - 1)
        return 1 + 2 * n * (n - 1)

def coloredCells(n: int) -> int:
    return Solution().coloredCells(n)