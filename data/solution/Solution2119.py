import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # If the number is 0, it will remain 0 after any number of reversals.
        # If the number ends with a zero (but is not zero itself), it will lose the trailing zeros after the first reversal.
        # Therefore, it will not be the same after two reversals.
        return num == 0 or num % 10 != 0

def isSameAfterReversals(num: int) -> bool:
    return Solution().isSameAfterReversals(num)