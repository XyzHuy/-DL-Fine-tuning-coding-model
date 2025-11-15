import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # We want to maximize the sum, so we should pick as many 1s as possible first.
        if k <= numOnes:
            return k
        # If we need more items after picking all 1s, we pick 0s (which don't change the sum).
        elif k <= numOnes + numZeros:
            return numOnes
        # If we still need more items, we pick -1s, which decrease the sum.
        else:
            return numOnes - (k - numOnes - numZeros)

def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    return Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)