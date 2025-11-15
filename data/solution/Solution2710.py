import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # Use the rstrip method to remove trailing zeros
        return num.rstrip('0')

def removeTrailingZeros(num: str) -> str:
    return Solution().removeTrailingZeros(num)