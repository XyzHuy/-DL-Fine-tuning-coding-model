import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # The idea is to find the number of ways to write n as the sum of consecutive numbers.
        # If we have k consecutive numbers starting from x, then the sum is:
        # x + (x + 1) + (x + 2) + ... + (x + k - 1) = kx + (0 + 1 + 2 + ... + k - 1) = kx + k(k - 1)/2
        # This should be equal to n: kx + k(k - 1)/2 = n => kx = n - k(k - 1)/2 => x = (n - k(k - 1)/2) / k
        # For x to be a positive integer, (n - k(k - 1)/2) must be positive and divisible by k.
        count = 0
        k = 1
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
            k += 1
        return count

def consecutiveNumbersSum(n: int) -> int:
    return Solution().consecutiveNumbersSum(n)