import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def thousandSeparator(self, n: int) -> str:
        return format(n, ',').replace(',', '.')

def thousandSeparator(n: int) -> str:
    return Solution().thousandSeparator(n)