import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def generateTheString(self, n: int) -> str:
        # If n is odd, we can return a string with all the same character repeated n times
        if n % 2 == 1:
            return 'a' * n
        # If n is even, we can return a string with 'a' repeated (n-1) times and 'b' once
        else:
            return 'a' * (n - 1) + 'b'

def generateTheString(n: int) -> str:
    return Solution().generateTheString(n)