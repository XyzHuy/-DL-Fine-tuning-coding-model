import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canWinNim(self, n: int) -> bool:
        # If n is a multiple of 4, you will always lose if both play optimally.
        # Otherwise, you can always win.
        return n % 4 != 0

def canWinNim(n: int) -> bool:
    return Solution().canWinNim(n)