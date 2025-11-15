import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1  # This is 2^n - 1
        
        if k == (length // 2) + 1:
            return "1"
        elif k < (length // 2) + 1:
            return self.findKthBit(n - 1, k)
        else:
            # k is in the last part, find the corresponding bit in the first part
            # and invert it
            corresponding_k = length - k + 1
            return "1" if self.findKthBit(n - 1, corresponding_k) == "0" else "0"

def findKthBit(n: int, k: int) -> str:
    return Solution().findKthBit(n, k)