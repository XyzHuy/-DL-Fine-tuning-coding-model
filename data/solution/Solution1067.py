import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count_digit(n: int, digit: int) -> int:
            count = 0
            power_of_10 = 1
            while n >= power_of_10:
                current = (n // power_of_10) % 10
                higher = n // (power_of_10 * 10)
                lower = n % power_of_10

                if current > digit:
                    count += (higher + 1) * power_of_10
                elif current == digit:
                    count += higher * power_of_10 + lower + 1
                else:
                    count += higher * power_of_10

                if digit == 0:
                    count -= power_of_10

                power_of_10 *= 10
            return count

        return count_digit(high, d) - count_digit(low - 1, d)

def digitsCount(d: int, low: int, high: int) -> int:
    return Solution().digitsCount(d, low, high)