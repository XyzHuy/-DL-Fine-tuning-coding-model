import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        # The number of distinct strings we can obtain is determined by the number of possible
        # substrings of length k that we can flip. Each flip operation on a substring of length k
        # can either be applied or not applied, leading to 2^(len(s) - k + 1) possible combinations.
        num_combinations = 1 << (len(s) - k + 1)  # This is equivalent to 2^(len(s) - k + 1)
        
        # Return the result modulo 10^9 + 7
        return num_combinations % (10**9 + 7)

def countDistinctStrings(s: str, k: int) -> int:
    return Solution().countDistinctStrings(s, k)