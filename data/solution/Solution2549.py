import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distinctIntegers(self, n: int) -> int:
        # After the first day, the number n will generate numbers from 2 to n-1 that satisfy x % i == 1
        # For example, if n = 5, then 5 % 2 == 1 and 5 % 4 == 1, so 2 and 4 are added.
        # The next day, 4 % 3 == 1, so 3 is added.
        # This process will eventually include all numbers from 2 to n.
        # Therefore, the number of distinct integers on the board after 10^9 days is n-1.
        # If n is 1, the only number on the board is 1, so the result is 1.
        return max(1, n - 1)

def distinctIntegers(n: int) -> int:
    return Solution().distinctIntegers(n)