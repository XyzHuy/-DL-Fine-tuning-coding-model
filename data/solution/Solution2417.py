import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def closestFair(self, n: int) -> int:
        def is_fair(k: int) -> bool:
            digits = str(k)
            even_count = sum(1 for d in digits if int(d) % 2 == 0)
            odd_count = len(digits) - even_count
            return even_count == odd_count

        # Start from the given number n
        while True:
            num_digits = len(str(n))
            # If the number of digits is odd, the next possible fair number
            # must have an even number of digits, so we skip to the next even length
            if num_digits % 2 != 0:
                n = 10 ** num_digits
            else:
                if is_fair(n):
                    return n
                n += 1

def closestFair(n: int) -> int:
    return Solution().closestFair(n)