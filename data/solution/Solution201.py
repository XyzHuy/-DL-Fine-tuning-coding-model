import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix bits
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Append zeros to the right
        return left << shift

def rangeBitwiseAnd(left: int, right: int) -> int:
    return Solution().rangeBitwiseAnd(left, right)